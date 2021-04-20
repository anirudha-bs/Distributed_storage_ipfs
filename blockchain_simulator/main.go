package main

import (
	"log"
	"sync"
	"time"

	"github.com/davecgh/go-spew/spew"
	"github.com/joho/godotenv"
)

// Struct to represent items of blocks
type Block struct {
	Index     int
	Timestamp string
	Key       int
	Hash      string
	PrevHash  string
}

var Blockchain []Block

type Message struct {
	Key int
}

// Mutex for locking purpose
var mutex = &sync.Mutex{}

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal(err)
	}

	// Adding genesis block
	go func() {
		t := time.Now()
		genesisBlock := Block{}
		genesisBlock = Block{0, t.String(), 0, calculateHash(genesisBlock), ""}
		spew.Dump(genesisBlock)

		mutex.Lock()
		Blockchain = append(Blockchain, genesisBlock)
		mutex.Unlock()
	}()
	log.Fatal(run())

}
