#import required libraries
import web3 from Web3
import json

# we need a provider to talk to the node.
provider = 'https://bsc-dataseed.binance.org/'
#create an instance for provider
w3 = Web3(Web3.HTTPProvider(provider)
# We need contract address import any contract address from bsc
contract_address = ''#insert contract address
# we need abi inorder to use contract functions
abi = json.loads('')#put the smart contract abi
#create contract instance
contract = w3.eth.contract(address = contract_address, abi = abi)
# now that we have created contract instance you can call contract functions
name = contract.functions.name().call()
totalsupply = contract.functions.totalSupply().call()
# lets make a transfer 
# we need 2 address for making transfer sender and receiver
sender = '' #put sender address
receiver = '' #put receiver address
# in order to make a transaction you need to sign transaction. to sign a transaction we need private key
pk_send = '' # put private key
      
amount_to_send = 1000
          
#Build Transaction
transfer_tx = contract.functions.transfer(receiver, w3.toWei(amount, 'ether').buildTransaction({
'chainId': 56,
'gas': = 210000,
'gasprice': = w3.toWei(10,'gwei'),
'nonce': = w3.eth.getTransactionCount(sender)
  })
                                          
 #sign transaction 
 tx_sign = w3.eth.account.signTransaction(transfer_tx,pk_send)
 
#send a transaction
                                          
send_tx = w3.eth.sendRawTransaction(tx_sign.rawTransaction)
print(send_tx)
                           



