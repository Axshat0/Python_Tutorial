#Variable scope
name = "takemichi" #global scope

def display_name():
  name = "Hanagaki" #local scope
  print(name)

display_name()
print(name)

#L = local
#E = enclosing
#G = global
#B = built-in 
