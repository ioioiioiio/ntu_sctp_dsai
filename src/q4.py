def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if the input is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    
    # Return the reversed string using slicing
    return s[::-1]

# Task 2: Invoke the function with given scenarios
# Case 1
result1 = string_reverse("Hello World")
print(result1)  # Expected output: "dlroW olleH"

# Case 2
result2 = string_reverse("Python")
print(result2)  # Expected output: "nohtyP"
