def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key exists in the dictionary
    if key in dct:
        print(f"Key '{key}' already exists with value: {dct[key]}")
    
    # Update the dictionary with the new key-value pair
    dct[key] = value
    
    # Return the updated dictionary
    return dct

# Task 2: Invoke the function with given scenarios
# Case 1
result1 = update_dictionary({}, "name", "Alice")
print(result1)  # Result: {"name": "Alice"}

# Case 2
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)  # Result: Key 'age' already exists with value: 25
                # {"age": 26}
