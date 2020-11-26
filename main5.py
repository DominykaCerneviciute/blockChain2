import hashlib
from struct import pack, unpack, unpack_from
from bitcoin.rpc import RawProxy
p = RawProxy()

a = int(input("Iveskite bloko numeri: "))
blockhash = p.getblockhash(a)
block = p.getblock(blockhash)

version = pack('<I', block['version']).encode('hex_codec')
prevBlockHash = block['previousblockhash'].decode('hex')
prevBlockHash = prevBlockHash[::-1].encode('hex_codec')
rootHash = block['merkleroot'].decode('hex')
rootHash = rootHash[::-1].encode('hex_codec')
time = pack('<I', block['time']).encode('hex_codec')
bits = pack('<I', int(block['bits'], 16)).encode('hex_codec')
nonce = pack('<I', block['nonce']).encode('hex_codec')

header_hex = (version + prevBlockHash + rootHash + time + bits + nonce)
header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
hash.encode('hex_codec')
print ("Gautas hash: " + hash[::-1].encode('hex_codec'))
print ("Bloko hash: " + blockhash)