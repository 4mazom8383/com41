#Find the folder path
import os
path = os.getcwd()
print(f"Current Working Folder Path: {path}")

#Folder content
for file in os.listdir(path):
  print(file)

print("")
print("")
print("")

def cwd():
  
  path = os.getcwd()
  print(f"Current Working Folder Path: {path}")
  print("The folder contains the following:")
  for file in os.listdir(path):
    print(file)   

def run():
  print("Processing...")
  cwd()

run()