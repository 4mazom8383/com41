# Ask user for number
print("How many numbers should I sum up?")
sum_numbers= int(input())

# Declare a control variable
number = 0

# Sum numbers
total = 0

while(number < sum_numbers):
  number = number + 1
  
  print("Please enter number 1 of", sum_numbers, ":")
  entred_number= int(input())
  
  total = total + entred_number

print("The answer is", total)  