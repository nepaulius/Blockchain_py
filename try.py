

from bitcoin.rpc import RawProxy
from operator import attrgetter

p = RawProxy()

def count_fee(temp):

	decoded_tx = p.decoderawtransaction(trans)
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




