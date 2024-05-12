import time

# Function to calculate the sum of all numbers from 1 to N
def calculate_sum_up_to(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def main():
    # Define the value of N
    n = 1000000000

    # Mark the start time
    start_time = time.time()

    # Call the function to calculate the sum
    result = calculate_sum_up_to(n)

    # Mark the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    print("Sum result up to {}: {}".format(n, result))
    print("Elapsed time: {:.6f} seconds".format(elapsed_time))
