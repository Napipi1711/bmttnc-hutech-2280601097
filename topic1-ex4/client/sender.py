def send_transaction(transaction):
    if transaction is None or transaction.signature is None:
        return False

    amount = int(transaction.amount)  
    sender = transaction.sender

   
    if sender.balance < amount:
        return False  

    
    sender.balance -= amount

    transaction.sent = True
    transaction.confirmed = True 
    return True
