# Define a string variable 'name'
name = "akshat singh!"

# Find and print the length of the string 'name'
print(len(name))

# Check if the first character (index 0) of 'name' is lowercase
if name[0].islower():
    # Capitalize the first letter of 'name' and print it
    name = name.capitalize()
    print(name)

# Extract and assign the uppercase part of the first name (index 0 to 5)
first_name = name[:6].upper()

# Extract and assign the lowercase part of the last name (index 7 to 11)
last_name = name[7:12].lower()

# Extract and assign the last character of the string 'name'
last_character = name[-1]

# Print the results
print(first_name)      # Uppercase first name: "AKSHAT"
print(last_name)       # Lowercase last name: "singh"
print(last_character)  # Last character: "!"
