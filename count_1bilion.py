import threading
import time


# Function to count numbers in a range
def count_numbers(start, end):
    for i in range(start, end):
        pass  # Do nothing, just counting


# Constants
TOTAL_COUNT = 1_000_000_000
NUM_THREADS = 8  # Adjust the number of threads as needed

# Calculate range for each thread
chunk_size = TOTAL_COUNT // NUM_THREADS
ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(NUM_THREADS)]
ranges[-1] = (
    ranges[-1][0],
    TOTAL_COUNT,
)  # Adjust the last range to cover the remainder

# Create threads
threads = []
for start, end in ranges:
    thread = threading.Thread(target=count_numbers, args=(start, end))
    threads.append(thread)
    thread.start()

# Measure time taken
start_time = time.time()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Calculate time taken
end_time = time.time()
time_taken = end_time - start_time

print(f"Counting to {TOTAL_COUNT} completed.")
print(f"Time taken: {time_taken:.2f} seconds.")
