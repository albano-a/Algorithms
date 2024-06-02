import time
from datetime import timedelta

start_time = time.time()

# Count to 100 million
for i in range(100_000_000):
    pass

end_time = time.time()

# Calculate the duration
duration = timedelta(seconds=end_time - start_time)

print(f"Time taken: {duration}")
