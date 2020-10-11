print("How old are you?")
age = int(input())

print("What is your nationality")
nationality = input()

if((nationality == "moroccan") or (nationality == "algerian") and (age <= 25)):
  print("You're an african youth")
else:
  print("You don't belong to the African continent")