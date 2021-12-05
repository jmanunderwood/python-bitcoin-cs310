from bitcoin.rpc import RawProxy

url=None
port=18332
conf="/home/user/.bitcoin/bitcoin.conf"

proxy = RawProxy(url,port,conf)

print("Enter account label, ")
print("or leave empty to list transactions")
print("for all accounts on the machine")
account_label = input(": ")

if account_label=="":
     account_label = "*"
transactions=proxy.listtransactions(account_label)

print(transactions)
