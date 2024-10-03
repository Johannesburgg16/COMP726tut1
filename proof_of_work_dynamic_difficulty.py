import hashlib
import random
import time

# Simplified Proof-of-Work function with difficulty adjustment
def proof_of_work(difficulty, target_time):
    target = 2 ** (256 - difficulty)  # Difficulty adjusts the target value
    nonce = random.randint(0, int(1e9))  # Random starting nonce
    block_found = False
    attempts = 0  # Count the number of attempts
    
    start_time = time.time()  # Record the start time

    while not block_found:
        # Generate hash for current nonce
        hash_result = hashlib.sha256(str(nonce).encode()).hexdigest()
        
        # Convert hash to a number (since it's hex)
        hash_value = int(hash_result, 16)
        
        # Check if the hash meets the target difficulty
        if hash_value < target:
            block_found = True
        else:
            nonce += 1  # Increment the nonce and try again
            attempts += 1
    
    end_time = time.time()  # Record the end time
    time_taken = end_time - start_time  # Calculate how long it took to find the block
    
    # Adjust difficulty
    if time_taken < target_time:
        difficulty += 1  # Increase difficulty if block found too quickly
        print(f"Block found too fast! Increasing difficulty to {difficulty}")
    elif time_taken > target_time:
        difficulty -= 1  # Decrease difficulty if block found too slowly
        print(f"Block found too slow! Decreasing difficulty to {difficulty}")
    
    return attempts, hash_result, time_taken, difficulty

# Set the initial difficulty and target time
difficulty = 20  # Start with a higher difficulty to make it more likely the block is found too slow
target_time = 10  # Set a lower target time for block discovery

# Run the proof-of-work script with difficulty adjustment
print(f"Starting Proof-of-Work with Difficulty {difficulty}")
attempts, final_hash, time_taken, new_difficulty = proof_of_work(difficulty, target_time)

print(f"\nResults:\nAttempts: {attempts}\nFinal Hash: {final_hash}\nTime Taken: {time_taken:.2f} seconds\nNew Difficulty: {new_difficulty}")
