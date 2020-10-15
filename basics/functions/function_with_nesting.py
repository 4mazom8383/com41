#Function
def identify():
  
  print("A word representing what you see")
  seen = input()

  if(seen.lower() == "a large boulder"):
    print("It's time to run!")
  else:
    print("We will be fine.")

# Calling function
identify()