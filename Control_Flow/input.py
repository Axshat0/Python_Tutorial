# User inputs
# Use the input() function to receive input from the user and store it in a variable.
name = input("What is your name ? : ")
age = int(input("How old are you ? : "))
height = float(input("How tall are you ? : "))

age = int(age)
height = float(height)

print("Hello " + name)
print("You're " + str(age) + " year old")
print("You're " + str(height) + "cm tall")
