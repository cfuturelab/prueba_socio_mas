import hashlib

def sha256(dataNeedSha):
    sha256 = hashlib.sha256()
    sha256.update(dataNeedSha.encode('utf-8'))
    return sha256.hexdigest()

# 区块
class Block:
    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.hash = self.ComputeHash

    @property
    def ComputeHash(self):
        return str(sha256(self.data))

    def showBlock(self):
        print ({'data':self.data, 'previousHash': self.previousHash, 'hash': self.hash})


# 链
class Chain:
    def __init__(self):
        self.chain = [self.ancestorBlock]

    @property
    def ancestorBlock(self):
        ancestor_block = Block('祖先区块', '')
        return ancestor_block

    @property
    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlockToChain(self, newBlock):
        newBlock.previousHash = self.getLatestBlock.hash
        newBlock.hash = newBlock.ComputeHash
        self.chain.append(newBlock)

    def showChain(self):
        for i in self.chain:
            i