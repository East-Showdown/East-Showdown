package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"sort"
	"strings"
	"sync"
	"time"
)

const wipDir = "./wip"

// CreateWIPFiles generates WIP files for translation using CheckResult
func CreateWIPFiles(ui map[string]string, result *CheckResult, bench bool) error {
	start := time.Now()
	cfg := result.Config

	printSeparator('=', 42)
	fmt.Println(ui["create_header"])
	printSeparator('=', 42)
	fmt.Println()

	// Clean and recreate WIP directory
	if _, err := os.Stat(wipDir); err == nil {
		fmt.Println(ui["cleaning_wip"])
		os.RemoveAll(wipDir)
	}
	os.MkdirAll(wipDir, 0755)

	fmt.Println(Blue + ui["creating_wip"] + Reset)
	fmt.Println()

	// Group keys by target file
	type fileData struct {
		targetFile string
		sourceFile string
		keys       []string
	}
	fileGroups := make(map[string]*fileData)

	for _, key := range result.MissingKeys {
		sourceFile, ok := result.KeyToFile.Get(key)
		if !ok {
			continue
		}
		targetFile := strings.Replace(sourceFile, cfg.SourceSuffix, cfg.TargetSuffix, 1)

		fd, exists := fileGroups[targetFile]
		if !exists {
			fd = &fileData{
				targetFile: targetFile,
				sourceFile: sourceFile,
				keys:       make([]string, 0, 64),
			}
			fileGroups[targetFile] = fd
		}
		fd.keys = append(fd.keys, key)
	}

	// Process files in parallel
	workers := runtime.NumCPU()
	jobs := make(chan *fileData, len(fileGroups))
	results := make(chan string, len(fileGroups))
	var wg sync.WaitGroup

	// Start workers
	for w := 0; w < workers; w++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for fd := range jobs {
				err := writeWIPFile(cfg, fd.targetFile, fd.sourceFile, fd.keys)
				if err != nil {
					results <- fmt.Sprintf("Error: %s - %v", fd.targetFile, err)
				} else {
					results <- fd.targetFile
				}
			}
		}()
	}

	// Send jobs
	for _, fd := range fileGroups {
		jobs <- fd
	}
	close(jobs)

	// Collect results in separate goroutine
	go func() {
		wg.Wait()
		close(results)
	}()

	// Print created files
	filesCreated := 0
	for result := range results {
		if strings.HasPrefix(result, "Error:") {
			fmt.Printf("%s%s%s\n", Red, result, Reset)
		} else {
			fmt.Printf("%s %s\n", Green+ui["created"]+Reset, result)
			filesCreated++
		}
	}

	// Count total keys
	totalKeys := 0
	for _, fd := range fileGroups {
		totalKeys += len(fd.keys)
	}

	// Summary
	fmt.Println()
	printSeparator('=', 42)
	fmt.Println(ui["summary"])
	printSeparator('=', 42)
	fmt.Printf("%s %d\n", Green+ui["files_created"]+Reset, filesCreated)
	fmt.Printf("%s %d\n", Green+ui["total_keys"]+Reset, totalKeys)
	fmt.Println()
	fmt.Printf("%s %s\n", Yellow+ui["files_location"]+Reset, wipDir)
	fmt.Println()

	// Instructions
	fmt.Println(Blue + ui["instructions"] + Reset)
	fmt.Println(ui["instruction1"])
	if cfg.SourceSuffix == "_l_russian.yml" {
		fmt.Println(ui["instruction2_rus_eng"])
		fmt.Println(ui["instruction3_rus_eng"])
	} else {
		fmt.Println(ui["instruction2_eng_rus"])
		fmt.Println(ui["instruction3_eng_rus"])
	}
	fmt.Println()

	if bench {
		fmt.Printf("%sBenchmark: %v%s\n", Yellow, time.Since(start), Reset)
	}

	return nil
}

func writeWIPFile(cfg DirectionConfig, targetFile, sourceFile string, keys []string) error {
	wipPath := filepath.Join(wipDir, targetFile)
	sourcePath := filepath.Join(cfg.SourceDir, sourceFile)

	// Load all full lines from source file in one pass
	keyLines := make(map[string]string, len(keys))

	// Create a set of keys we need for fast lookup
	neededKeys := make(map[string]struct{}, len(keys))
	for _, k := range keys {
		neededKeys[k] = struct{}{}
	}

	// Read source file once
	f, err := os.Open(sourcePath)
	if err != nil {
		return err
	}

	scanner := bufio.NewScanner(f)
	scanner.Buffer(make([]byte, 64*1024), 64*1024)

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line == "" || line[0] == '#' {
			continue
		}

		colonIdx := strings.IndexByte(line, ':')
		if colonIdx <= 0 {
			continue
		}

		key := strings.TrimSpace(line[:colonIdx])
		if _, needed := neededKeys[key]; needed {
			keyLines[key] = line
		}
	}
	f.Close()

	if err := scanner.Err(); err != nil {
		return err
	}

	// Build output
	var sb strings.Builder
	sb.Grow(len(keys) * 100) // estimate 100 bytes per line

	sb.WriteString(fmt.Sprintf("# %s\n", getCreditsLine()))
	sb.WriteString(cfg.TargetTag + "\n")

	// Sort keys for consistent output
	sortedKeys := make([]string, len(keys))
	copy(sortedKeys, keys)
	sort.Strings(sortedKeys)

	for _, key := range sortedKeys {
		if fullLine, ok := keyLines[key]; ok {
			sb.WriteString(" " + fullLine + "\n")
		} else {
			sb.WriteString(fmt.Sprintf(" %s: \"[TRANSLATION NEEDED]\"\n", key))
		}
	}

	return os.WriteFile(wipPath, []byte(sb.String()), 0644)
}
