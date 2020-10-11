print("How far are we from the cave?")
distance = int(input())


for count in range(distance, 0, -1):
  print(count, "steps remaining")


print("")


for count in range(0, distance, 1):
  print(count, "steps remaining")