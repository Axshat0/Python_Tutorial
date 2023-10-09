#Nested looops :
#loops inside other loops. They are used for iterating through multiple levels of data

# Prompt the user to enter the number of rows and columns.
rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter a symbol to use: ")

# Outer loop iterates over the rows.
for i in range(rows):
    # Inner loop iterates over the columns.
    for j in range(columns):
        # Print the symbol, use 'end=""' to prevent automatic newline.
        print(symbol, end="")
    
    # After printing all columns in a row, move to the next line.
    print()
