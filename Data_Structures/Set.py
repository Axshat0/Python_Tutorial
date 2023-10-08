#Set
#sets are unordered collections of unique elements
utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#pop(random)
#remove and return the last item from a list
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

#add a single item to the set
utensils.add("Oil")
print(utensils)
#add more than one item
utensils.update(dishes)
print(utensils)
#remove items form Set
utensils.remove("spoon")
print(utensils)
#all unique elements from both sets (no duplicates)
set = utensils.union(dishes)
print(set)
#modifying 'utensils'
utensils.update(dishes)
print(utensils)
#prints only items that are similar
set1 = utensils.intersection(dishes)
print(set1)
utensils.intersection_update(dishes)
print(utensils)
#not similar to both the sets
set2 = utensils.symmetric_difference(dishes)
print(set2)
utensils.symmetric_difference_update(dishes)
print(utensils)
#only items that are only present in the original set
set3 = utensils.difference(dishes)
print(set3)
#checks if items of given set are present in another set
print(utensils.isdisjoint(dishes))
print(utensils.issuperset(dishes))

for x in utensils:
  print(x)
