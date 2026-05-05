package main

import (
	"sync"
)

const numShards = 256

// ShardedSet is a lock-free-ish concurrent set using sharding
// Each shard has its own mutex, reducing contention to 1/256
type ShardedSet struct {
	shards [numShards]shard
}

type shard struct {
	mu   sync.RWMutex
	data map[string]struct{}
}

// NewShardedSet creates a new sharded set with preallocated maps
func NewShardedSet(estimatedSize int) *ShardedSet {
	ss := &ShardedSet{}
	perShard := estimatedSize / numShards
	if perShard < 16 {
		perShard = 16
	}
	for i := range ss.shards {
		ss.shards[i].data = make(map[string]struct{}, perShard)
	}
	return ss
}

// getShard returns shard index based on first byte of key
// This is faster than hashing the entire string
func (ss *ShardedSet) getShard(key string) *shard {
	if len(key) == 0 {
		return &ss.shards[0]
	}
	return &ss.shards[key[0]]
}

// Add adds a key to the set
func (ss *ShardedSet) Add(key string) {
	s := ss.getShard(key)
	s.mu.Lock()
	s.data[key] = struct{}{}
	s.mu.Unlock()
}

// Contains checks if key exists in set
func (ss *ShardedSet) Contains(key string) bool {
	s := ss.getShard(key)
	s.mu.RLock()
	_, ok := s.data[key]
	s.mu.RUnlock()
	return ok
}

// Keys returns all keys as a slice (for iteration)
func (ss *ShardedSet) Keys() []string {
	// Count total first
	total := 0
	for i := range ss.shards {
		ss.shards[i].mu.RLock()
		total += len(ss.shards[i].data)
		ss.shards[i].mu.RUnlock()
	}

	result := make([]string, 0, total)
	for i := range ss.shards {
		ss.shards[i].mu.RLock()
		for k := range ss.shards[i].data {
			result = append(result, k)
		}
		ss.shards[i].mu.RUnlock()
	}
	return result
}

// Len returns total number of elements
func (ss *ShardedSet) Len() int {
	total := 0
	for i := range ss.shards {
		ss.shards[i].mu.RLock()
		total += len(ss.shards[i].data)
		ss.shards[i].mu.RUnlock()
	}
	return total
}

// Difference returns keys in ss that are not in other
// This is parallelized across shards
func (ss *ShardedSet) Difference(other *ShardedSet) []string {
	var wg sync.WaitGroup
	results := make([][]string, numShards)

	for i := range ss.shards {
		wg.Add(1)
		go func(idx int) {
			defer wg.Done()
			s := &ss.shards[idx]
			s.mu.RLock()
			defer s.mu.RUnlock()

			var diff []string
			for k := range s.data {
				if !other.Contains(k) {
					diff = append(diff, k)
				}
			}
			results[idx] = diff
		}(i)
	}

	wg.Wait()

	// Merge results
	total := 0
	for _, r := range results {
		total += len(r)
	}
	merged := make([]string, 0, total)
	for _, r := range results {
		merged = append(merged, r...)
	}
	return merged
}

// KeyToFileMap is a concurrent map for key->filename mapping
type KeyToFileMap struct {
	shards [numShards]kvShard
}

type kvShard struct {
	mu   sync.RWMutex
	data map[string]string
}

func NewKeyToFileMap(estimatedSize int) *KeyToFileMap {
	m := &KeyToFileMap{}
	perShard := estimatedSize / numShards
	if perShard < 16 {
		perShard = 16
	}
	for i := range m.shards {
		m.shards[i].data = make(map[string]string, perShard)
	}
	return m
}

func (m *KeyToFileMap) getShard(key string) *kvShard {
	if len(key) == 0 {
		return &m.shards[0]
	}
	return &m.shards[key[0]]
}

func (m *KeyToFileMap) Set(key, value string) {
	s := m.getShard(key)
	s.mu.Lock()
	s.data[key] = value
	s.mu.Unlock()
}

func (m *KeyToFileMap) Get(key string) (string, bool) {
	s := m.getShard(key)
	s.mu.RLock()
	v, ok := s.data[key]
	s.mu.RUnlock()
	return v, ok
}
