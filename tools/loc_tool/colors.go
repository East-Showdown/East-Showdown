package main

// ANSI color codes - inlined for zero overhead
const (
	Red    = "\033[0;31m"
	Green  = "\033[0;32m"
	Yellow = "\033[1;33m"
	Blue   = "\033[0;34m"
	Reset  = "\033[0m"
)

// Precomputed colored strings for common outputs
var (
	checkMark = Green + "✓" + Reset
	crossMark = Red + "✗" + Reset
)
