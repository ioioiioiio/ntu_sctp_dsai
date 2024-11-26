def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Initialize index variable
    index = 0
    
    # Loop through the list using while loop
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]  # Return the first negative number
        index += 1
    
    # If no negative number is found, return the message
    return "No negatives"

# Task 2: Invoke the function with given scenarios
# Case 1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(result1)  # Expected output: -1 (first negative number)

# Case 2
result2 = find_first_negative([2, 10, 7, 0])
print(result2)  # Expected output: "No negatives" (no negative numbers in the list)
