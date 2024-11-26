def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if lst is a list
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    # Replace occurrences of find_val with replace_val
    lst = [replace_val if item == find_val else item for item in lst]
    
    # Return the modified list
    return lst

# Task 2: Invoke the function with given scenarios
# Case 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)  # Result: [1, 5, 3, 4, 5, 5]

# Case 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)  # Result: ["orange", "banana", "orange"]
