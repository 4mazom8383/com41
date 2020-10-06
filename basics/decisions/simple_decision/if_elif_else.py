# check whether first number is bigger than the second number.
# Assume first_number and second_number are existing variables.

print("please enter first number")
first_number = input()

print("please enter second number")
second_number = input()

if (first_number > second_number):
  print("First is bigger!")
elif (first_number < second_number):
  print("First is smaller!")    
else:
  print("Both are equal!")
print("Done!")




print("\nPlease identify who you are")
entity = input()
if (entity == "Human"):
  print("You are a human!")
elif (entity == "Robot"):
  print("You are a robot!")
elif (entity == "Animal"):
  print("You are an animal!")
else:
  print("I do not know what you are!")

print("Analysis complete.")




print("\nTowards which direction should I paint (up, down, left or right)?")
direction = input()

if(direction == "up"):
  print("I am painting in the upward direction!")
elif(direction == "back"):
  print("I am painting in the backward direction!")
elif(direction == "right"):
  print("I am painting in the right direction!")
elif(direction == "left"):
  print("I am painting in the left direction!")

