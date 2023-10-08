#Loop control
# This is an infinite loop using 'while True'
while True:
    name = input("Enter your name : ")
    # Check if the 'name' is not an empty string
    if name != "":
        # If 'name' is not empty, exit the loop using 'break'
        break

# Define a phone number string
phone_number = "123-456-7890"

# Iterate through each character in 'phone_number'
for i in phone_number:
    # Check if the current character is a hyphen "-"
    if i == "-":
        # If it's a hyphen, skip this iteration and continue to the next character
        continue
    # Print the current character without a newline, using 'end=""'
    print(i, end="")

# Iterate through numbers from 1 to 20 using 'range(1, 21)'
for i in range(1, 21):
    # Check if the current number is 13
    if i == 13:
        # If it's 13, do nothing and continue to the next iteration (using 'pass')
        pass
    else:
        # If it's not 13, print the current number
        print(i)
