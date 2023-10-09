# String slicing

#[start:stop:step]

name = "Naruto Uzumaki"
print(len(name))              # Print the length of the name
first_name = name[:6]        # Get the first name
last_name = name[7:]         # Get the last name
funky_name = name[::3]       # Get every third character
print(first_name)
print(last_name)
print(funky_name)

# Slice
website = "http://google.com"
website1 = "http://wikipedia.com"

slice = slice(7, -4)         # Create a slice object
print(website[slice])        # Apply slice to the website
print(website1[slice])       # Apply slice to website1
