import datetime
import hashlib


class Block:
    blockNo = 0
    data = None
    next = None
    hash = None

    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.utcnow()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )

        return h.hexdigest()

    def __str__(self):
        return f"Block Hash: {str(self.hash())} \n BlockNo: {str(self.blockNo)} \n Block Data: {str(self.data)} \n Hashed: {str(self.nonce)}\n"


class BlockChain:
    diff = 20
    maxNonce = 2 ** 32
    target = 2 ** (256 - diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


blockchain = BlockChain()
for n in range(1000):
    blockchain.mine(Block(f"Block {n + 1}"))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
