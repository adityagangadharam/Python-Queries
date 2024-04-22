import time
import sys

for i in range(100):
    # Print the message followed by a carriage return.
    sys.stdout.write(f"\rYour progress message or number here: {i}")

    # Make sure to flush the output to ensure the line is updated in real time.
    sys.stdout.flush()

    # Wait for a bit before the next update (simulating your progress updates)
    time.sleep(0.1)

# Print a newline character at the end to move to the next line once your loop is done.
print()