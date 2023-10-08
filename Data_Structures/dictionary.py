#Dictionary :
#dictionary variables are data structures that store key-value pairs, 
#allowing you to access values by their associated keys. They are defined using curly braces
#{Key:value}
capitals = {
  "USA" : "washington DC",
  "India" : "New dehli",
  "China" : "Beijing",
  "Russia" : "Mascow"
}

for key,value in capitals.items():
  print(key, value)

ep = {122: 45, 123: 14, 124: 90 }

for x in capitals:
  print(x)

#clear all items from the 'capitals' dictionary
capitals.clear()
# Remove and return the item at index 122
ep.pop(122)
print(ep)
#Remove and return an arbitrary (usually the last) key-value pair
capitals.popitem()
# Delete the key 'USA'
del capitals['USA']
#Update the 'capitals' dictionary with a new key-value pair
capitals.update({"USA":"Tokyo"})

print(capitals)

