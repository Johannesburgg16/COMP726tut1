# Hashrate of Bitcoin network in hashes per second (e.g., 300 Exahashes per second)
network_hashrate = 300 * 10**18  # 300 EH/s

# Replace this with your PC's measured hashrate (from the output of the previous script)
your_hashrate = 1937072.34  # Example: 2 million hashes per second

# Calculate time to find a block (in seconds)
time_to_find_block = (network_hashrate / your_hashrate) * 600

# Convert the time to more readable units (e.g., years)
time_in_years = time_to_find_block / (60 * 60 * 24 * 365)

print(f"Estimated time to find a block: {time_in_years:.2f} years")
