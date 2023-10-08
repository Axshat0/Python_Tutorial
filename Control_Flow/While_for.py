#While loop
# Code to be executed as long as the condition is True

name = ""
while len(name) == 0:
  name = input("Enter your name : ")
print("Hello "+ name)

#_________OR____________

# Initialize the 'name' variable as None
name = None
# Create a while loop that continues until 'name' has a non-empty value
while not name:
    name = input("Enter your name: ")

print("Hello " + name)

#for loop
# for i in range(10):
#   print(i)

# for i in "Nami":
#   print(i)

# for i in range(50, 100+1, 2):
#   print(i)



# Import the 'time' module to work with time-related functions
import time
# Use a 'for' loop to count down from 10 to 1
for seconds in range(10, 0, -1):
    print(seconds)  # Print the current count
    time.sleep(1)   # Pause the program for 1 second
    
print("Happy New Year !")

