#Exception handling
#Events detecting during execution that interrupt the flow of a program

try:
   numerator = int(input("Enter a number to divide : "))
   denominator = int(input("Enter a number to divide by : "))
   result = numerator/denominator
  
# Handle a ZeroDivisionError if the user tries to divide by zero.
except ZeroDivisionError:
  print("You can't divide by zero! idiot!")

# Handle a ValueError if the user enters something that cannot be converted to an # integer.
except ValueError:
  print("Enter only number plz")

# Handle any other exceptions (errors) that might occur.
except Exception as e:
  print(e)
  print("Somthing went wrong :( ")
else:
  print(result)
