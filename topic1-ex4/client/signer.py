from rsa_utils import sign_data

def sign_transaction(transaction, private_key):
    data = f"{transaction.sender.name}{transaction.receiver}{transaction.amount}".encode()
    transaction.signature = sign_data(private_key, data)