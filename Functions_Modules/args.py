# *args
# Define a function 'add' that takes two parameters 'num1' and 'num2'
def add(num1, num2):
    sum = num1 + num2
    return sum

# Call the 'add' function with arguments 1 and 2, and print the result
print(add(1, 2))  # Output: 3

# Redefine the 'add' function using *args to accept a variable number of arguments
def add(*args):
    sum = 0
    # Convert 'args' (which is a tuple) to a list for manipulation
    args = list(args)
    # Set the first element of the list to 0
    args[0] = 0
    # Iterate through the 'args' list and calculate the sum of all elements
    for i in args:
        sum += i
    # Return the final sum
    return sum

# Call the new 'add' function with multiple arguments (1, 2, 3, 4, 5, 6) and print the result
print(add(1, 2, 3, 4, 5, 6))  # Output: 21
