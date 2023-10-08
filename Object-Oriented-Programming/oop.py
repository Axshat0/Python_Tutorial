'''Object-Oriented Programming : a way of organizing code where you create reusable "objects" (like blueprints) with both data (attributes) and actions (methods) to model real-world entities'''

#first make a folder called massages or whatever you want 
# Define a class named Car
class Car:

  wheel = 4 # Number of wheels for all cars (a class-level attribute)

  def __init__(self, make, model, year, color):
      self.make = make      # Instance variable for the car's make
      self.model = model    # Instance variable for the car's model
      self.year = year      # Instance variable for the car's manufacturing year
      self.color = color    # Instance variable for the car's color
    
  def drive(self):
    print("The "+ self.model +" is driving")
  
  def stop(self):
    print("The " + self.model +" is stoped")

# Write - from (whatever your file name is) import (the modeul name)

from massages import Car


# Create two Car objects with different attributes
car_1 = Car("chevy","corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_2.stop()

# Change the 'wheel' attribute for car_2 (applies only on car_2 )
car_2.wheel = 2 
print(car_2.wheel)
print(car_1.wheel)

# Change the 'wheel' attribute for the Car class (applies to all Car objects)
Car.wheel = 2
print(car_2.wheel)
print(car_1.wheel)

