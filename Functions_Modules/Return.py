#used within functions to send a value back to the caller. 
#It allows functions to produce output that can be used in other parts of the program or assigned to variables for further processing.
#Return statement
def multiply(number1, number2):
  result = number1 * number2
  return result

def multiply(number1, number2):
   return number1 * number2

print(multiply(3,9))
x = multiply(25, 5)
print(x)
