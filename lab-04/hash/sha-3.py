from Crypto.Hash import SHA3_256

def sha3_256_hash(input_string):
    sha3_256 = SHA3_256.new()
    sha3_256.update(input_string.encode('utf-8'))
    return sha3_256.hexdigest()

def main():
    text = input("nhap chuoi text: ").encode('utf-8')
    hashed_text = sha3(text)
    
    print("CHuoi van ban da nhap: ",text.decode('utf-8'))
    print("SHA-3-hash: ",hashed_text.hex())
    
if __name__ == "__main__":
    main()    