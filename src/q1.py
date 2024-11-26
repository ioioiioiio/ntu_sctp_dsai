
def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y are not numeric.
    - Print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap values without using a third variable
    x, y = y, x

    # Print swapped values
    print(f"Swapped values: x = {x}, y = {y}")

    # Return swapped values (optional)
    return x, y

# Task 2: Invoke the function with given scenarios
# Scenario 1: "Apple", 10
result1 = swap("Apple", 10)
print(result1)  # Result: -1 (non-numeric)

# Scenario 2: 9, 17
result2 = swap(9, 17)
print(result2)  # Result: Swapped values: x = 17, y = 9
                # (and the tuple (17, 9) as return value)
