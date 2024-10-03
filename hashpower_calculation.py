import hashlib
import time

def calculate_hashpower(num_hashes):
    start_time = time.time()  # Start time
    for i in range(num_hashes):
        hashlib.sha256(str(i).encode()).hexdigest()
    end_time = time.time()  # End time
    
    # Calculate time taken and hashrate
    time_taken = end_time - start_time
    hashpower = num_hashes / time_taken  # Hashes per second
    return hashpower, time_taken

# Define how many hashes to compute
num_hashes = 1000000  # 1 million hashes

# Calculate hashpower
hashrate, time_taken = calculate_hashpower(num_hashes)

print(f"Performed {num_hashes} hashes in {time_taken:.2f} seconds")
print(f"Your PC's hash rate is: {hashrate:.2f} hashes per second")
