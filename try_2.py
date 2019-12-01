
# `pc_transaction.py` example
from bitcoin.rpc import RawProxy

import hashlib
import codecs
import base64
import struct

p = RawProxy()

def indians(temp):
	a=struct.pack("<I",temp)
	b=codecs.encode(a,'hex')
	c=b.decode()
	return c

def SwapOrder(temp):

	S_array=[]
	Reverse=temp[::-1]
	Split=list(Reverse)	
	a=""
	for i in range(0,len(Split),2):
		a+=Split[i+1]+Split[i]
	
	return a


blockheight = 277316


blockhash = p.getblockhash(blockheight)


block = p.getblock(blockhash)

version=indians(block['version'])
prev_hash=SwapOrder(block['previousblockhash'])
merkle_root=SwapOrder(block['merkleroot'])
time_stamp=indians(block['time'])
d_bits=SwapOrder(block['bits'])
nonce=indians(block['nonce'])



first_hex=(version+prev_hash+merkle_root+time_stamp+d_bits+nonce)

header_bin=codecs.decode(first_hex, 'hex')

hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()

hash3=codecs.encode(hash[::-1],'hex_codec')



print(" ")
print("Block hash : ")
print(blockhash)
print(" ")
print("Block hash after verification : ")
print(hash3.decode())
print(" ")

