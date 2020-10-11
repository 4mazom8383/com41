print("While EXMAPLE")  
count = 0
while (count < 2):
  print("#########")
  print("#       #")
  print("# O   O #")
  print("|   V   |")
  print("|  ---  |")
  print("|_______|")

  count = count +1

print("")
print("FOR EXMAPLE")  

for count in range(0, 2, 1):
  print("#########")
  print("#       #")
  print("# O   O #")
  print("|   V   |")
  print("|  ---  |")
  print("|_______|")

print("")

print("How many mountains should I display?")
mountains= int(input())
 
print("Displaying...")
for count in range(0, mountains, 1):
  print("         __          ")
  print("        /  \_        ")
  print("        /^    \      ")
  print("      /  ^    \_     ")
  print("    _/ ^ ^     ^\    ")
  print("    /  ^     ^    \  ")
