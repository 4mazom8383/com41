import random

print("Please enter the minimum value:")
min_value = int(input())

print("Please enter the maximum value:")
max_value = int(input())

random_number = random.randrange(min_value, max_value)

print("\nI am thinking of a number between {} and {}. \nCan you guess what it is?" .format(min_value, max_value))

#print(random_number)

guess = 0

while (guess != random_number):
  print("Please enter a number:")
  guess = int(input())
  if(guess < random_number):
    print("Your guess is too low\n")
  elif(guess > random_number):
    print("Your guess is too high\n")
  elif(guess == random_number):
    print("Congratulations!")
    break

print("Game over!")


