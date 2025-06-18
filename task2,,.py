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