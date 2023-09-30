import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions):
        self.index = index  # Position of the block in the blockchain
        self.previous_hash = previous_hash
        self.timestamp = timestamp  # Timestamp indicating when the block was created
        self.transactions = transactions  # List of transactions included in the block
        self.current_hash = self.calculateHash()  # Hash of the block itself

    # Method calculates the hash of the block
    def calculateHash(self):
        data = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.transactions)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    # Creates the genesis block with index 0, a previous hash of "0," and a timestamp based on the current time
    def createGenesisBlock(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    # Adds a new block to the blockchain. It sets the previous hash of the new block to the current hash of the
    # last block in the chain and recalculates the current hash of the new block.
    def addBlock(self, new_block):
        new_block.previous_hash = self.chain[-1].current_hash
        new_block.current_hash = new_block.calculateHash()
        self.chain.append(new_block)
