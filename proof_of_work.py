import hashlib
import random

# Simplified Proof-of-Work function
def proof_of_work(difficulty):
    target = 2 ** (256 - difficulty)  # Difficulty adjusts the target value
    nonce = random.randint(0, int(1e9))  # Random starting nonce, converted to integer
    block_found = False
    attempts = 0  # Count the number of attempts
    
    while not block_found:
        # Generate hash for current nonce
        hash_result = hashlib.sha256(str(nonce).encode()).hexdigest()
        
        # Convert hash to a number (since it's hex)
        hash_value = int(hash_result, 16)
        
        # Check if the hash meets the target difficulty
        if hash_value < target:
            block_found = True
            print(f"Block found! Nonce: {nonce}, Hash: {hash_result}")
        else:
            nonce += 1  # Increment the nonce and try again
            attempts += 1
    
    return attempts, hash_result

# Run the simplified Proof-of-Work at two difficulty levels
difficulty_1 = 20  # Lower difficulty (easier)
difficulty_2 = 22  # Higher difficulty (harder)

print("Running Proof-of-Work with Difficulty 1:")
attempts_1, final_hash_1 = proof_of_work(difficulty_1)

print("\nRunning Proof-of-Work with Difficulty 2:")
attempts_2, final_hash_2 = proof_of_work(difficulty_2)

print(f"\nResults:\nDifficulty 1 - Attempts: {attempts_1}, Final Hash: {final_hash_1}")
print(f"Difficulty 2 - Attempts: {attempts_2}, Final Hash: {final_hash_2}")
