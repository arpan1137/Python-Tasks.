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
