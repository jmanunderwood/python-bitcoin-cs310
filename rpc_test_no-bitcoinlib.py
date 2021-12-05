import rpc_request as rq

print("Enter account label, ")
print("or leave empty to list transactions")
print("for all accounts on the machine")
account_label=input(": ")

if account_label=="":
     account_label = "*"
transactions=rq.send_request("listtransactions", account_label)

print(transactions)
