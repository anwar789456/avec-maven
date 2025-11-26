def factorial(n):
    # Factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test the function
test_value = 5
print(f"Factorial of {test_value} is:", factorial(test_value))
