#logical operators

temp = int(input("What is the temperatur out side? : "))

# Assume temp is a variable that holds the current temperature

# Using the first condition
if temp >= 0 and temp <= 30:
    print("The temperature is good today")
    print("Go outside!")

# Using the first condition with an "elif" (else if) statement, which is not applicable
elif temp < 0 and temp > 30:
    print("The temperature is bad today")
    print("Stay inside!")

# not
# Using the negation of the first condition
if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today")
    print("Stay inside!")

# Using the negation of the first condition with an "elif" statement, which is not applicable
elif not(temp < 0 and temp > 30):
    print("The temperature is good today")
    print("Go outside!")
