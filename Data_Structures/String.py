# String methods

# The '\n' in the string represents a newline character and will break the text into two lines when printed.
print(name)
name = "naruto \n uzumaki"

str = "naruto uzumaki"
print(str.upper())        # Convert to uppercase
print(str.lower())        # Convert to lowercase
print(str.capitalize())   # Capitalize the first letter
print(str.center(50, "."))  # Center the string with dots
print(str.count("a"))     # Count occurrences of 'a'
print(str.find("i"))      # Find the index of 'i'
print(str.replace("H", "M"))  # Replace 'H' with 'M'
print(str.endswith("!!!"))  # Check if it ends with "!!!"

# More string methods
str1 = "Hello !!!"
print(str1.rstrip("!"))   # Remove trailing '!'
print(str1.replace("H", "M"))  # Replace 'H' with 'M'
print(str1.endswith("!!!"))  # Check if it ends with "!!!
