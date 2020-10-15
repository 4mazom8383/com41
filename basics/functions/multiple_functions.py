def display_ladder(steps):
  #Display each step
  for count in range(steps):
    print("| |")
    print("***")
    print("")

def create_ladder():
  print("How many steps remain?")
  steps = int(input())
  display_ladder(steps)


#Calling second function
create_ladder()