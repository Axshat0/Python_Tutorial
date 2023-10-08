#if else elif

# Get the user's age as input and convert it to an integer
age = int(input("How old are you : "))

# Check if age is greater than or equal to 100
if age >= 100:
    print("You are a century old !")  # If true, print this

# Check if age is greater than or equal to 18 (but less than 100)
elif age >= 18:
    print("You are an adult !")  # If true, print this

# Check if age is negative (less than 0)
elif age < 0:
    print("You haven't been born yet !")  # If true, print this

# If none of the above conditions are met, the age is between 0 and 17
else:
    print("You are a child !")  # If true, print this
