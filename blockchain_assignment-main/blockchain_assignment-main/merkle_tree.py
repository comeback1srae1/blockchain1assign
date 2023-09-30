import hashlib

class MerkleNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self.createTree(transactions)

    def createTree(self, transactions):
        if len(transactions) == 0:
            return None
        if len(transactions) == 1:
            return MerkleNode(transactions[0])

        nodes = [MerkleNode(tx) for tx in transactions]

        while len(nodes) > 1:
            new_level = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i + 1] if i + 1 < len(nodes) else left
                combined_data = left.data + right.data
                combined_hash = hashlib.sha256(combined_data.encode()).hexdigest()
                parent_node = MerkleNode(combined_hash)
                parent_node.left = left
                parent_node.right = right
                new_level.append(parent_node)
            nodes = new_level

        return nodes[0]

    def addTransaction(self, transaction_data):
        self.transactions.append(transaction_data)
        self.root = self.createTree(self.transactions)

    def getRootHash(self):
        return self.root.data if self.root else None
