# ask user what to do
print("What should I do (play/study)?")
activity = input()
    
# decide if beep should play or study
if (activity == "play"):

  # ask user what to play with
  print("What should I play with (toy/friend)?")
  play_with = input()
  
  # decide if beep should play with toys or friend
  if (play_with == "toy"):
    print("I will play with my toys!")
  else:
    print("I will play with my friend!")


else:
  print("I will study")



#Code Two
print("\nWhat type of cover does the book have?")
book = input()

if(book == "soft"):
  print("Is the book perfect-bound?")
  perfect_bound = input()

  if(perfect_bound == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books")

elif (book == "hard"):
  print("Books with hard covers can be more expensive!")

