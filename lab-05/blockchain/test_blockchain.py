from blockchain import Blockchain


my_blockchain = Blockchain()

my_blockchain.add_transaction('Alice', 'Bob', 10)
my_blockchain.add_transaction('Bob', 'Charlie', 5)
my_blockchain.add_transaction('Charlie', 'Alice', 3)

pervious_block = my_blockchain.get_previous_block()
pervious_proof = pervious_block.proof
new_proof = my_blockchain.proof_of_work(pervious_proof)
pervious_hash = pervious_block.hash
my_blockchain.add_transaction('Genesis','Miner', 1)
new_block = my_blockchain.create_block(new_proof, pervious_hash)

for block in my_blockchain.chain:
    print(f"block #{block.index}")
    print("Timestamp", block.timestamp)
    print("Transactions", block.transactions)
    print("Proof", block.proof)
    print("Previous Hash", block.previous_hash)
    print("Hash", block.hash)
    print("--------------")
    
print("Is blockchain valid?", my_blockchain.is_chain_valid(my_blockchain.chain))
    