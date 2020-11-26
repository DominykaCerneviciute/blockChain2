from bitcoin.rpc import RawProxy
p = RawProxy()

txid = input("Iveskite tranaskcijos hash: ")
raw_tx = p.getrawtransaction(txid)
decoded_tx = p.decoderawtransaction(raw_tx)
tx_value = 0
for output in decoded_tx['vout']:
    tx_value = tx_value + output['value']
print("Outputs: ", tx_value)
input_tx_value = 0
for input in decoded_tx['vin']:
        input_raw_tx = p.getrawtransaction(input['txid'])
        input_decoded_tx = p.decoderawtransaction(input_raw_tx)
        for output in input_decoded_tx['vout']:
            input_tx_value = input_tx_value + output['value']
print("Inputs: ", input_tx_value)
fee = input_tx_value - tx_value
print ("Transaction fee: ", fee)
