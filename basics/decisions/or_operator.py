# Retrieve shape from user
print("What shape do I have?")
shape = input()
    
# Identify the shape
if ((shape == "square") or (shape == "rectangle") or (shape == "rhombus")):
  print("This shape is a parallelogram.")
else:
  print("This shape is not a parallelogram.")




# Type of adventure
print("\nWhat type of adventure should I have?")
adventure = input()
    
# Identify the shape
if ((adventure == "scary") or (adventure == "short")):
  print("Entering the dark forest!")

elif ((adventure == "safe") or (adventure == "long")):
  print("Taking the safe route!")

else:
  print("Not sure which route to take.")