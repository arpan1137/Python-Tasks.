# Python-Tasks.
#Task 1
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Sample number
sample_number=5

# Call the factorial function and print the result
result = factorial(sample_number)
print(f"The factorial of {sample_number} is {result}")
#Task 2
import math

# 1. Ask the user for a number as input
number = float(input("Enter a number: "))

# 2. Perform calculations using the math module
sqrt_result = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)  # Input should be in radians

# 3. Display the calculated results
print(f"Square root of {number} = {sqrt_result}")
print(f"Natural logarithm of {number} = {log_result}")
print(f"Sine of {number} (in radians) = {sine_result}")
