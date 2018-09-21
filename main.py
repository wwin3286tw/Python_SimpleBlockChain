import hashlib
class Block():
  def __init__(self, index, previousHash, timestamp, data, hash):
   self.name = name
   self.previousHash = previousHash
   self.timestamp = timestamp
   self.data = data
   self.hash = hash
def calculateHash(index, previousHash, timestamp, data):
 return hashlib.sha256(str(index).encode() + str(previousHash).encode() + str(timestamp).encode() + str(data).encode()).hexdigest()
#print(calculateHash(1,156,'5','gr'))
