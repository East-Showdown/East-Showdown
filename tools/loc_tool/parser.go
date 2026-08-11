package main

import (
	"bufio"
	"bytes"
	"os"
	"sync"
)

const (
	scannerBufferSize = 64 * 1024 // 64KB buffer for scanner
)

// bufferPool reuses byte slices to reduce allocations
var bufferPool = sync.Pool{
	New: func() interface{} {
		b := make([]byte, scannerBufferSize)
		return &b
	},
}

// FileParseResult contains parsed data from a single file
type FileParseResult struct {
	Filename string
	Keys     []string
	KeyLines map[string]string // key -> full line (for WIP generation)
	Err      error
}

// ParseFile reads a YML file and extracts localization keys
// Uses zero-copy techniques where possible
func ParseFile(filepath, filename, langTag string, needFullLines bool) FileParseResult {
	result := FileParseResult{
		Filename: filename,
		Keys:     make([]string, 0, 256), // preallocate for typical file
	}
	if needFullLines {
		result.KeyLines = make(map[string]string, 256)
	}

	f, err := os.Open(filepath)
	if err != nil {
		result.Err = err
		return result
	}
	defer f.Close()

	// Get buffer from pool
	bufPtr := bufferPool.Get().(*[]byte)
	defer bufferPool.Put(bufPtr)

	scanner := bufio.NewScanner(f)
	scanner.Buffer(*bufPtr, scannerBufferSize)

	langTagBytes := []byte(langTag)

	for scanner.Scan() {
		line := scanner.Bytes()

		// Skip empty lines
		if len(line) == 0 {
			continue
		}

		// Skip comments (lines starting with # after trimming)
		trimmed := bytes.TrimLeft(line, " \t")
		if len(trimmed) == 0 || trimmed[0] == '#' {
			continue
		}

		// Skip language tag line
		if bytes.Contains(trimmed, langTagBytes) {
			continue
		}

		// Find key (everything before first ':')
		colonIdx := bytes.IndexByte(trimmed, ':')
		if colonIdx <= 0 {
			continue
		}

		keyBytes := trimmed[:colonIdx]

		// Validate key starts with letter or underscore
		if !isValidKeyStart(keyBytes[0]) {
			continue
		}

		// Convert to string (unavoidable allocation, but only for valid keys)
		key := string(keyBytes)
		result.Keys = append(result.Keys, key)

		if needFullLines {
			// Store full line for WIP generation
			result.KeyLines[key] = string(bytes.TrimSpace(trimmed))
		}
	}

	if err := scanner.Err(); err != nil {
		result.Err = err
	}

	return result
}

// isValidKeyStart checks if byte is a valid key starting character
// Inlined for performance
func isValidKeyStart(b byte) bool {
	return (b >= 'A' && b <= 'Z') || (b >= 'a' && b <= 'z') || b == '_'
}

// FindFullLine searches for a specific key's full line in a file
// Optimized for single key lookup
func FindFullLine(filepath, key string) (string, bool) {
	f, err := os.Open(filepath)
	if err != nil {
		return "", false
	}
	defer f.Close()

	keyPrefix := []byte(key + ":")

	bufPtr := bufferPool.Get().(*[]byte)
	defer bufferPool.Put(bufPtr)

	scanner := bufio.NewScanner(f)
	scanner.Buffer(*bufPtr, scannerBufferSize)

	for scanner.Scan() {
		line := scanner.Bytes()
		trimmed := bytes.TrimLeft(line, " \t")

		if bytes.HasPrefix(trimmed, keyPrefix) {
			return string(bytes.TrimSpace(trimmed)), true
		}
	}

	return "", false
}

// ParseFilesConcurrent parses multiple files in parallel
func ParseFilesConcurrent(dir string, files []string, langTag string, needFullLines bool, workers int) []FileParseResult {
	if workers <= 0 {
		workers = 4
	}

	results := make([]FileParseResult, len(files))
	jobs := make(chan int, len(files))
	var wg sync.WaitGroup

	// Start workers
	for w := 0; w < workers; w++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for i := range jobs {
				filepath := dir + "/" + files[i]
				results[i] = ParseFile(filepath, files[i], langTag, needFullLines)
			}
		}()
	}

	// Send jobs
	for i := range files {
		jobs <- i
	}
	close(jobs)

	wg.Wait()
	return results
}
