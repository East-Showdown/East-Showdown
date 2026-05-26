package main

import (
	"fmt"
	"os"
	"runtime"
	"sort"
	"strings"
	"time"
)

const reportFile = "localization_report.txt"

// Direction represents comparison direction
type Direction int

const (
	RusToEng Direction = iota
	EngToRus
)

// DirectionConfig holds direction-specific settings
type DirectionConfig struct {
	SourceDir    string
	TargetDir    string
	SourceTag    string
	TargetTag    string
	SourceSuffix string
	TargetSuffix string
	SourceLang   string
	TargetLang   string
}

func GetDirectionConfig(dir Direction) DirectionConfig {
	if dir == RusToEng {
		return DirectionConfig{
			SourceDir:    "./russian",
			TargetDir:    "./english",
			SourceTag:    "l_russian:",
			TargetTag:    "l_english:",
			SourceSuffix: "_l_russian.yml",
			TargetSuffix: "_l_english.yml",
			SourceLang:   "RUS",
			TargetLang:   "ENG",
		}
	}
	return DirectionConfig{
		SourceDir:    "./english",
		TargetDir:    "./russian",
		SourceTag:    "l_english:",
		TargetTag:    "l_russian:",
		SourceSuffix: "_l_english.yml",
		TargetSuffix: "_l_russian.yml",
		SourceLang:   "ENG",
		TargetLang:   "RUS",
	}
}

// CheckResult contains the results of localization check
type CheckResult struct {
	Config          DirectionConfig
	SourceKeys      *ShardedSet
	TargetKeys      *ShardedSet
	MissingKeys     []string
	KeyToFile       *KeyToFileMap
	SourceFileCount int
	TargetFileCount int
	Percentage      int
	Duration        time.Duration
}

// CheckLocalization performs the localization completeness check
func CheckLocalization(ui map[string]string, dir Direction, writeReport bool, bench bool) (*CheckResult, error) {
	start := time.Now()
	cfg := GetDirectionConfig(dir)
	workers := runtime.NumCPU()

	// Print header
	printSeparator('=', 42)
	fmt.Println(ui["check_header"])
	printSeparator('=', 42)
	fmt.Println()

	// Validate directories
	if _, err := os.Stat(cfg.SourceDir); os.IsNotExist(err) {
		return nil, fmt.Errorf("%s %s", ui["error_source_dir"], cfg.SourceDir)
	}
	if _, err := os.Stat(cfg.TargetDir); os.IsNotExist(err) {
		return nil, fmt.Errorf("%s %s", ui["error_target_dir"], cfg.TargetDir)
	}

	fmt.Println(Blue + ui["step1_merge"] + Reset)
	fmt.Println()

	// Get source files
	sourceFiles, err := getYMLFiles(cfg.SourceDir)
	if err != nil {
		return nil, err
	}

	// Get target files
	targetFiles, err := getYMLFiles(cfg.TargetDir)
	if err != nil {
		return nil, err
	}

	// Parse source files in parallel
	fmt.Printf("%s (%s)...\n", ui["processing_source"], cfg.SourceLang)
	sourceResults := ParseFilesConcurrent(cfg.SourceDir, sourceFiles, cfg.SourceTag, true, workers)

	// Build source keys set and key-to-file map
	sourceKeys := NewShardedSet(40000)
	keyToFile := NewKeyToFileMap(40000)

	for _, res := range sourceResults {
		if res.Err != nil {
			fmt.Printf("%sError reading %s: %v%s\n", Red, res.Filename, res.Err, Reset)
			continue
		}
		for _, key := range res.Keys {
			sourceKeys.Add(key)
			keyToFile.Set(key, res.Filename)
		}
	}
	fmt.Printf("  %s %d\n", Green+ui["processed_source"]+Reset, len(sourceFiles))
	fmt.Println()

	// Parse target files in parallel
	fmt.Printf("%s (%s)...\n", ui["processing_target"], cfg.TargetLang)
	targetResults := ParseFilesConcurrent(cfg.TargetDir, targetFiles, cfg.TargetTag, false, workers)

	// Build target keys set
	targetKeys := NewShardedSet(40000)
	for _, res := range targetResults {
		if res.Err != nil {
			fmt.Printf("%sError reading %s: %v%s\n", Red, res.Filename, res.Err, Reset)
			continue
		}
		for _, key := range res.Keys {
			targetKeys.Add(key)
		}
	}
	fmt.Printf("  %s %d\n", Green+ui["processed_target"]+Reset, len(targetFiles))
	fmt.Println()

	// Step 2: Compare keys
	fmt.Println(Blue + ui["step2_compare"] + Reset)
	fmt.Println()

	sourceCount := sourceKeys.Len()
	targetCount := targetKeys.Len()

	fmt.Printf("  %s %d\n", Green+ui["unique_source"]+Reset, sourceCount)
	fmt.Printf("  %s %d\n", Green+ui["unique_target"]+Reset, targetCount)
	fmt.Println()

	// Calculate missing keys (parallel difference)
	missingKeys := sourceKeys.Difference(targetKeys)
	sort.Strings(missingKeys)

	missingCount := len(missingKeys)

	if missingCount == 0 {
		fmt.Printf("  %s\n", Green+ui["all_keys_present"]+Reset)
		fmt.Println()
		printSeparator('=', 42)
		fmt.Println(ui["localization_complete"])
		printSeparator('=', 42)

		duration := time.Since(start)
		if bench {
			fmt.Printf("\n%sBenchmark: %v%s\n", Yellow, duration, Reset)
		}

		return &CheckResult{
			Config:          cfg,
			SourceKeys:      sourceKeys,
			TargetKeys:      targetKeys,
			MissingKeys:     missingKeys,
			KeyToFile:       keyToFile,
			SourceFileCount: len(sourceFiles),
			TargetFileCount: len(targetFiles),
			Percentage:      100,
			Duration:        duration,
		}, nil
	}

	fmt.Printf("  %s %d\n", Red+ui["missing_keys_found"]+Reset, missingCount)
	fmt.Println()

	percentage := 0
	if sourceCount > 0 {
		percentage = ((sourceCount - missingCount) * 100) / sourceCount
	}
	fmt.Printf("%s %s%d%%%s\n", ui["completion"], Yellow, percentage, Reset)
	fmt.Println()

	// Step 3: Show missing keys grouped by file
	fmt.Println(Blue + ui["step3_search"] + Reset)
	fmt.Println()

	// Generate report (to file if requested, always to console)
	err = printMissingKeys(ui, cfg, missingKeys, keyToFile, writeReport)
	if err != nil {
		return nil, err
	}

	// Summary
	printSeparator('=', 42)
	fmt.Println(ui["summary"])
	printSeparator('=', 42)
	fmt.Printf("%s %s%d%%%s\n", ui["localization_completion"], Yellow, percentage, Reset)
	fmt.Printf("%s %s%d%s\n", ui["missing_keys"], Red, missingCount, Reset)
	fmt.Println()

	if writeReport {
		fmt.Printf("%s %s\n", Green+ui["report_saved"]+Reset, reportFile)
	}

	duration := time.Since(start)
	if bench {
		fmt.Printf("\n%sBenchmark: %v%s\n", Yellow, duration, Reset)
	}

	return &CheckResult{
		Config:          cfg,
		SourceKeys:      sourceKeys,
		TargetKeys:      targetKeys,
		MissingKeys:     missingKeys,
		KeyToFile:       keyToFile,
		SourceFileCount: len(sourceFiles),
		TargetFileCount: len(targetFiles),
		Percentage:      percentage,
		Duration:        duration,
	}, nil
}

func getYMLFiles(dir string) ([]string, error) {
	entries, err := os.ReadDir(dir)
	if err != nil {
		return nil, err
	}

	files := make([]string, 0, len(entries))
	for _, e := range entries {
		if !e.IsDir() && strings.HasSuffix(e.Name(), ".yml") {
			files = append(files, e.Name())
		}
	}
	sort.Strings(files)
	return files, nil
}

func printMissingKeys(ui map[string]string, cfg DirectionConfig, missingKeys []string, keyToFile *KeyToFileMap, writeReport bool) error {
	// Group by target file
	type fileGroup struct {
		keys []string
	}
	groups := make(map[string]*fileGroup)

	for _, key := range missingKeys {
		sourceFile, ok := keyToFile.Get(key)
		if !ok {
			continue
		}
		targetFile := strings.Replace(sourceFile, cfg.SourceSuffix, cfg.TargetSuffix, 1)

		g, exists := groups[targetFile]
		if !exists {
			g = &fileGroup{keys: make([]string, 0, 32)}
			groups[targetFile] = g
		}
		g.keys = append(g.keys, key)
	}

	// Sort file names for consistent output
	fileNames := make([]string, 0, len(groups))
	for f := range groups {
		fileNames = append(fileNames, f)
	}
	sort.Strings(fileNames)

	// Build report string only if writing to file
	var report *strings.Builder
	if writeReport {
		report = &strings.Builder{}
		report.Grow(64 * 1024)
		report.WriteString(fmt.Sprintf("Missing Localization Keys Report (%s -> %s)\n", cfg.SourceLang, cfg.TargetLang))
		report.WriteString(fmt.Sprintf("Created: %s\n", time.Now().Format(time.RFC3339)))
		report.WriteString(getCreditsLine() + "\n")
		report.WriteString(strings.Repeat("=", 40) + "\n\n")
		report.WriteString("STATISTICS:\n")
		report.WriteString(fmt.Sprintf("  Missing keys: %d\n\n", len(missingKeys)))
	}

	// Print to console (and optionally to report)
	for _, targetFile := range fileNames {
		g := groups[targetFile]
		sourceFile := strings.Replace(targetFile, cfg.TargetSuffix, cfg.SourceSuffix, 1)

		fmt.Printf("%s %s\n", Yellow+ui["file"]+Reset, targetFile)
		fmt.Printf("  %s %d\n", Red+ui["missing_in_file"]+Reset, len(g.keys))
		fmt.Printf("  %s %s/%s\n", Blue+ui["path_original"]+Reset, cfg.SourceDir, sourceFile)
		fmt.Printf("  %s %s/%s\n", Blue+ui["path_translation"]+Reset, cfg.TargetDir, targetFile)
		fmt.Println()

		if writeReport {
			report.WriteString(fmt.Sprintf("\nFILE: %s (%d keys)\n", targetFile, len(g.keys)))
			for _, k := range g.keys {
				report.WriteString(fmt.Sprintf("  - %s\n", k))
			}
		}
	}

	if writeReport {
		return os.WriteFile(reportFile, []byte(report.String()), 0644)
	}
	return nil
}

func printSeparator(char rune, length int) {
	fmt.Println(strings.Repeat(string(char), length))
}

func getCreditsLine() string {
	return fmt.Sprintf("Generated by %s's tool | %s | %s", author, project, motto)
}
