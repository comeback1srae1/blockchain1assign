import time
from merkle_tree import MerkleTree

def main():
    blockchain = blockchain()
    merkle_tree = MerkleTree([])

    while True:
        print("List of actions:")
        print("1. Add new transaction")  # Add new transaction to the Merkle tree
        print("2. Mine block")  # Mine a new block with transactions from the Merkle tree
        print("3. See the blockchain")  # Display the current state of the blockchain
        print("4. Exit")

        choice = input("What do you want to do? ")

        if choice == "1":
            data = input("Write transaction data: ")
            merkle_tree.addTransaction(data)
            print("Transaction added successfully\n")
        
        elif choice == "2":
            if len(merkle_tree.transactions) == 0:
                print("There are no transactions yet!")
            else:
                new_block = block(len(blockchain.chain), blockchain.chain[-1].current_hash, int(time.time()), merkle_tree.transactions)
                blockchain.addBlock(new_block)
                merkle_tree = MerkleTree([])  # Reset the tree after mining is done
                print("Block has been mined\n")
        
        elif choice == "3":
            for block in blockchain.chain:
                print(f"Index: {block.index}")
                print(f"Previous hash: {block.previous_hash}")
                print(f"Timestamp: {block.timestamp}")
                print(f"Transactions: {block.transactions}")
                print(f"Current hash: {block.current_hash}\n")
        
        elif choice == "4":
            break
        
        else:
            print("Invalid input. Please try again.\n")

if __name__ == "__main__":
    main()
