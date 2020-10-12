print("List numbers in line")
for number in range(0, 10, 1):
  print(number, "|", end="")
print("\n")


print("Three list of numbers in line")
for count in range(0, 3, 1):
  for number in range(0, 10, 1):
    print(number, "|", end="")
  print("\n")
  

print("")
print("")

print("\nHow many rows should I have?")
row = int(input())

print("How many columns should I have?")
columns = int(input())

print("Here I go:\n")
for count in range(0, row, 1):
  for number in range(0, columns, 1):
    print(":-) ", end="")
  print("\n")
  
print("Done!")