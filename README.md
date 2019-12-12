# Blockchain_py

**Pirmoji užduotis**

Vartotojas gali įvesti norimos transakcijos id ir gauti jos mokestį už jos siuntimą. Taip pat vartotojui automatiškai *print*'inamas brangiausios transakcijos mokestis.

* Programinio kodo veikias : vartotojui įvedus transakcijos *hash*'ą, vykdoma count_fee() funkcija, kuri dekoduoja transakcija ir iš kiekvieno *vin* gauną kitos transakcijos id ir jos *vout*'ą. Jei *n* ir kitos transakcijos *vout*'as sutampa *value* sumuojama. Transakcijos *vout*'ų *value* taip pat sumuojama, ir rezultatas gaunamas atėmus *vout* sumą  iš *vin*.
* Programos kodas:

```py
from bitcoin.rpc import RawProxy
from operator import attrgetter

p = RawProxy()

def count_fee(temp):

	decoded_tx = p.decoderawtransaction(temp)
	vin_value=0
	vout_value=0

	for i in decoded_tx['vin']:
		raw_tx = p.getrawtransaction(i['txid'])
		next_decoded = p.decoderawtransaction(raw_tx)
		vinVout=i['vout']
		for k in next_decoded['vout']:
			if(k['n']==vinVout):
				vin_value+=k['value']
	
	for output in decoded_tx['vout']:
		vout_value = vout_value + output['value']

	ans=vin_value-vout_value
	print("Transaction fee : ", ans, " BTC") 



txt=input("Enter your transaction hash :")
t = p.getrawtransaction(txt)
count_fee(t)

print("Biggest transaction fee : ")
trans=p.getrawtransaction('4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d')
count_fee(trans)

```

* Programos rezultatas :

![](https://user-images.githubusercontent.com/45967745/70716132-688eac00-1cf4-11ea-93f1-368e7b5a7b0e.png)

___

**Antroji užduotis**

Gaunamas bloko headerio info (version, previousblockhash, mekleroot, time, bits, nonce). Version, time ir nonce funkcijoje indians() paverčiami į liitle-endian. Previous hash, merkleroot, bits sumaišoma funkcijoje Swap_order(). Visi elementai sudedami į string'ą, kuris suhash'uojmas SHA-256 algoritmu 2 kartus.

* Programos kodas:

```py

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

```
* Programos rezultatas : 

![](https://user-images.githubusercontent.com/45967745/70718091-3e3eed80-1cf8-11ea-8615-b18d449490c1.png)

