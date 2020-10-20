#fruits = ["Apple","Banana","Orange"]

#for fruit in fruits:
#  print(fruit)

#for index in range(len(fruits)):
#  print("{} is at index {}.".format(fruit, index))

#List
def directions():
  directions = ["Move Forward","Move Backward","Turn Left", "Turn Right"]
  return directions

#Printing the list
def menu():
  print("Please select a direction")
  direction = directions()
  for index in range(len(direction)):
    #print("{} is at index {}.".format(direction[index],index))
    print("{} : {}".format(index,direction[index]))

#Run the list
def run ():
  menu()

run()