import time
import random

# Set the duration in seconds
duration = 0.7

# Get the current time
start_time = time.time()

# Loop until the specified duration has passed
while time.time() - start_time < duration:
    # Generate and display a random number
    x = random.randint(0, 9)
    print(x, end=' ')

    # Add a small delay between each number
    time.sleep(0.1)

# Print a new line after the sequence
print()

def list_pop():
    def list_pop():
        # Define the duration in seconds
        duration = 0.7

        # Generate and display the random number
        print(Guessing.generated_list, end=' ')

        # Add a delay of 0.7 seconds
        time.sleep(duration)

        # Print a new line after the sequence
        print()

list_pop()