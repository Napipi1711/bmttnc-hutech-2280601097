from rsa_utils import verify_signature

def verify_transaction(transaction, public_key):
    if transaction.signature is None:
        return False
    data = f"{transaction.sender.name}{transaction.receiver}{transaction.amount}".encode()
    return verify_signature(public_key, data, transaction.signature)