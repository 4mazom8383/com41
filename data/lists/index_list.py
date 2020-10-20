fruits = ["apple", 5, "banana", 10, "cherry", 15]

# Display the first item i.e. apple
#print(fruits[0])

# Update the second item i.e. replace banana with berry
fruits[2] = "berry"

# Remove the third item i.e. removes cherry
del fruits[2]

#print(fruits)



def movements():
  path = ["Move Forward",10,"Move Backward",5,"Move Left",3,"Move Right",1]
  return path

def run():
  print("Moving...")
  direction = movements()
  print("{} for {} steps".format(direction[0],direction[1]))
  print("{} for {} steps".format(direction[2],direction[3]))
  print("{} for {} steps".format(direction[4],direction[5]))
  print("{} for {} steps".format(direction[6],direction[7]))
  
run()
  
  #steps = path[1,3,5,7]
  #directions = path[0,2,4,6]
  #print("{} for {} steps".format(steps))
  #for steps in range():

