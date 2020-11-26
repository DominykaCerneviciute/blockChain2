import hashlib
from struct import pack, unpack, unpack_from
from bitcoin.rpc import RawProxy

p = RawProxy()

a = int(input("Iveskite bloko numeri: "))
blockhash = p.getblockhash(a)
block = p.getblock(blockhash)

version = pack('<I', block['version']).encode('hex')
prevBlockHash = (block['previousblockhash'].decode('hex'))[::-1].encode('hex')
rootHash = (block['merkleroot'].decode('hex'))[::-1].encode('hex')
time = pack('<I', block['time']).encode('hex')
bits = (block['bits'].decode('hex'))[::-1].encode('hex')
nonce = pack('<I', block['nonce']).encode('hex')

header_hex = (version + prevBlockHash + rootHash + time + bits + nonce)
header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()

print ("Gautas hash: " + hash[::-1].encode('hex'))
print ("Bloko hash: " + blockhash)