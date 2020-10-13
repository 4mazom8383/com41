print("Program Started!\nPlease enter a letter:")
letter = input() 

#print("The ASCII code for t is:", ord(letter))
#ord_letter = ord(letter)

if(len(letter) <= 1 ):
  print("The ASCII code for", letter ,"is:", ord(letter)  )
elif(len(letter) > 1):
  print("Sorry, the entered letter length is more than 1")

print("Program Ended!")