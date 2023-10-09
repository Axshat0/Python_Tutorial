# **Kwargs
# Define a function 'hello' that accepts two parameters 'first' and 'last'
def hello(first, last):
    print("Hello " + first + " " + last)

# Call the 'hello' function with keyword arguments
hello(first="eren", last="yeager")
# Output: Hello eren yeager

# Define a function 'hello' that accepts keyword arguments using **kwargs
def hello(**kwargs):
    # Print a greeting with values extracted from 'kwargs' dictionary
    print("Hello " + kwargs["first"] + " " + kwargs["last"])

# Call the 'hello' function with keyword arguments
hello(first="eren", last="yeager")
# Output: Hello eren yeager

# Define another 'hello' function using **kwargs, which allows any number of keyword arguments
def hello(**kwargs):
    print("Hello ", end=" ")
    # Iterate through 'kwargs' to print all values
    for key, value in kwargs.items():
        print(value, end=" ")

# Call the 'hello' function with keyword arguments
hello(first="eren", last="yeager")
# Output: Hello eren yeager

# Call the 'hello' function with additional keyword arguments
hello(title="Mr.", first="eren", last="yeager")
# Output: Hello Mr. eren yeager
