#Lists in python :
 #list is an ordered collection of items enclosed in square brackets, 
#allowing for elements of different data types and supporting various operations like indexing, slicing, and appending

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding", "spaghetti"]

#[start:stop:step]
print(food[:])
print(food[:5])
print(food[2:])
print(food[0:6:2])
print(food[2:6:2])

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]

#sorts the list in ascending order
food.sort()

#print the list in descending order
food.sort(reverse=True)

#This method reverses the order of the list.
food.reverse()

for x in food:
  print(x)

#returns the index of the "first occurrence" of the list item.
print(food.index("spaghetti"))

#Returns the count of the number of items with the given value
print(food.count("spaghetti"))

#Returns copy of the list. This can be done to perform operations on the list without modifying the original list
print(food.copy())

#appends items to the end of the existing list
food.append("ice cream")
print(food)

#adds an entire list or any other
food.extend(num)
print(food)
#Easy way
print(food + num)

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

# 2D lists

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice-cream"]

food = [drinks,dinner, dessert]

print(food[0][0])
print(food[1][2])
print(food[2][1])

#ETC (end of thinking capacity)
