print("Program Started!")
print("Please enter an ASCII code:")

code = int(input())

low = 32
high = 126

# check the code if it is positive and integer
if( (code == int(code)) and (code == abs(code)) ):
# check the code if it is in the range of 32 and 126
  if code in range(low, high):
    letter = chr(code)
    print("The character represented by the ASCII code {} is {}" .format (code,letter))

else:
  print("The entred values didn't meet the program requirments")

print("Program Ended!")