#1
# inheritance
class Animal:

  alive =True # Class-level attribute indicating all animals are alive by default
  def eat(self):
    print("This animal is eating")
    
  def sleep(self):
    print("This animal is sleeping")

# Define a subclass 'Rabbit' that inherits from 'Animal'
class Rabbit(Animal):
  # Method specific to rabbits
  def run(self):
    print("this rabbit is runnig")

# Define a subclass 'Fish' that also inherits from 'Animal'
class Fish(Animal):
  # Method specific to fish
  def swim(self):
    print("this fish is swimming")

# Define another subclass 'Hawk' that inherits from 'Animal'
class Hawk(Animal):
  # Method specific to hawks
  def fly(self):
    print("This hawk is flying")

# Create instances of the classes
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

#----------------------------------------------------------------------

#2
# Multiple inheritance
class Organism:
  alive = True # Class-level attribute indicating all organisms are alive by default

# Define a subclass 'Animal' that inherits from 'Organism'
class Animal(Organism):
  #(specific to animals)
  def eat(self):
    print("Thia animal is eating")

# Define another subclass 'Dog' that inherits from 'Animal'
class Dog(Animal):
  def bark(self):
    print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

#----------------------------------------------------------------------
#3
# Multiple inheritance
class Prey:
  def flee(self):
    print("This animal flees")

class Predator:
  def hunt(self):
    print("This animal hunting")

# Define a subclass 'Rabbit' that inherits from 'Prey'
class Rabbit(Prey):
  pass

# Define a subclass 'Hawk' that inherits from 'Predator'
class Hawk(Predator):
  pass

# Define a subclass 'Fish' that inherits from both 'Predator' and 'Prey'
class Fish(Predator,Prey):
  pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

fish.hunt()
fish.flee()

#----------------------------------------------------------------------

#4
#Over riding

class Animal:
  def eat(self):
    print("This animal is eating")

class Rabbit(Animal):
  # Define a subclass 'Rabbit' that inherits from 'Animal' and overrides the 'eat' method
class Rabbit(Animal):
  def eat(self):
   print("This rabbit is eating carrot")

rabbit = Rabbit()
# When you call the 'eat' method on the 'rabbit' instance, it uses the overridden implementation
rabbit.eat() 

#----------------------------------------------------------------------

#5
# chaining

class Car:
  def turn_on(self):
    print("You start the engine")
    return self

  
  def drive(self):
    print("You drive the car")
    return self
    
  def brake(self):
    print("You step on the brakes")
    return self
    
  def turn_off(self):
    print("You turn off the engine")
    return self

car = Car()

# Method calls without chaining
car.turn_on()
car.drive()

# Method chaining: You can call multiple methods on the same object in a single line
car.turn_on().drive()

# Method chaining with more methods
car.turn_on().drive().brake().turn_off()
