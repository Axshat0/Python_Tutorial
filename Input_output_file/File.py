#Before running the code, you should create the following files and folders in the same directory as your Python script

#1. Create a file named `test.txt`. You can create a plain text file using a text editor and add some text content to it.

#2. Optionally, create an empty folder named `empty_folder`. This folder should be empty, with no files or subfolders inside.

#3. Optionally, create a folder named `folder` and place some files or subfolders inside it. This folder should not be empty

#Ensure that these files and folders exist with the specified names and locations before running the code


#File detection 

help("modules")
# it shows you a list of all the tools and modules you can use


# Import the necessary libraries
import shutil
import os

# Define the path to the file or folder you want to work with
path = "test.txt"
if os.path.exists(path):
  print("That loction exists!")
  if os.path.isfile(path):
    print("That is a file")
  else:
    ("That is a directory")
else:
  ("That location doesn't exists!")

#Read a file


try:
    with open('test.txt') as file:
      print(file.read())
except FileNotFoundError:
  print("This file was not found :( ")

# Write to a file
text = "OMG! you can read this! have a nice day!"

with open("test.txt",'w') as file:
  file.write(text)

#Copy a file 
# copyfile() = copies containt os a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

shutil.copyfile("test.txt","copy.txt")   #src,dst

#Move a file

source = "test.txt"
destination = "C:\\User\\Cakow\\Desktop\\test.txt"

try:
  if os.path.exists(destination):
    print("There is already a file there")
  else:
    os.replace(source,destination)
    print(source +" was moved")
  
except FileNotFoundError:
  print(source +" was not found")
  
#Delete a file 

path = 'copy.txt'
path_efolder = 'empty_folder'
path_folder = 'folder'

try:
    os.remove(path)         # Delete a file
    os.rmdir(path_efolder)  # Delete an empty folder
    shutil.rmtree(path_folder)  # Delete a folder and its contents

except FileNotFoundError:
  print("This file was not found")
except PermissionError:
  print("You do not have permission to delete that")
except OSError:
  print("You cannot delete that using that function")

else:
  print("successfully deleted")
