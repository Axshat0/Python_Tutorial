#String formate 
animal = "Cow"
item = "Moon"

# Using {} as placeholders and .format() method to fill them with variables.
text = "The {} jumped over the {}"
print(text.format(animal, item))

print("The {} jumped over the {}".format(animal, item))

# Concatenating strings using + operator.
print("The " + animal + " jumped over the " + item)

# Using positional arguments to specify the order of variables.
print("The {1} jumped over the {0}".format(animal, item))

# Using keyword arguments to specify the values of variables.
print("The {item} jumped over the {animal}".format(animal="Cow", item="Moon"))  # Output: "The Moon jumped over the Cow"

name = "Eren"

# Basic string formatting with variable insertion.
print("Hello my name is {} ".format(name))

# Specifying a minimum width of 10 characters for the formatted string.
print("Hello my name is {:10}. Nice to meet you".format(name))  # Output: "Hello my name is Eren       . Nice to meet you"

# Right-aligning the formatted string within a 10-character width.
print("Hello my name is {:>10}. Nice to meet you".format(name))  # Output: "Hello my name is       Eren. Nice to meet you"

# Left-aligning the formatted string within a 10-character width.
print("Hello my name is {:<10}. Nice to meet you".format(name))  # Output: "Hello my name is Eren      . Nice to meet you"

# Center-aligning the formatted string within a 10-character width.
print("Hello my name is {:^10}. Nice to meet you".format(name))  # Output: "Hello my name is   Eren   . Nice to meet you"

x = 3.14159

# Formatting a floating-point number with two decimal places.
print("The number pi is {:.2f}".format(x))  # Output: "The number pi is 3.14"

y = 1000

# Formatting an integer with comma as a thousands separator.
print("The number is {:,}".format(y))  # Output: "The number is 1,000"

# Formatting an integer in binary, octal, and hexadecimal representations.
print("The number is {:b}".format(y))  # Output: "The number is 1111101000" (binary)
print("The number is {:o}".format(y))  # Output: "The number is 1750" (octal)
print("The number is {:X}".format(y))  # Output: "The number is 3E8" (hexadecimal)

# Formatting a number in scientific notation.
print("The number is {:E}".format(y)) 
