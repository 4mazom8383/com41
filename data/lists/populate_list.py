#List
def directions():
  directions = ["Move Forward","Move Backward","Turn Left", "Turn Right"]
  return directions

#Printing the list
def menu():
  print("Please select a direction")
  #selected_direction = int(input())
  direction = directions()
  for index in range(len(direction)):
    #print("{} is at index {}.".format(direction[index],index))
    print("{} : {}".format(index,direction[index]))



#Run the list
def run():
  #route = []
  print("Working out escape route...\n")

  for count in range(5):
    menu()
    print("")

  print("Escape route:", directions())


run()