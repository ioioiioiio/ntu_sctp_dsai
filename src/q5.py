def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both num and divisor are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise ValueError("Both num and divisor must be numeric.")
    
    # Check divisibility
    return num % divisor == 0

# Task 2: Invoke the function with given scenarios
# Case 1
result1 = check_divisibility(10, 2)
print(result1)  # Result: True (10 is divisible by 2)

# Case 2
result2 = check_divisibility(7, 3)
print(result2)  # Result: False (7 is not divisible by 3)
