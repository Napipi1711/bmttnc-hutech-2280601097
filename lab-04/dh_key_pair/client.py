from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


# Tạo cặp khóa DH cho client
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key


# Sinh shared secret từ private_key client + public_key server
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key


def main():
    # Load khóa public của server
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Lấy tham số DH từ khóa public server
    parameters = server_public_key.parameters()

    # Tạo khóa của client
    private_key, public_key = generate_client_key_pair(parameters)

    # Tạo shared secret
    shared_secret = derive_shared_secret(private_key, server_public_key)

    # In ra dưới dạng hex
    print("Shared Secret:", shared_secret.hex())


if __name__ == "__main__":
    main()
