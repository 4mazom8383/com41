def box(word):
  dashes = 5 + len(word)
  print("-" * dashes)
  print("| {} |".format(word))
  print("-" * dashes)

def lower_case(word):
  print(word.lower())


def upper_case(word):
  print(word.upper())


def mirrored(word):
  mirrored = ""
  for letter in reversed(word):
    mirrored += letter
  print("{} | {}".format(word, mirrored))


def reapt_word(word):
  print("How many times you want to display the word and then display the word")
  times = int(input())
  for count in range(times):
    print(word.lower())
    print(word.upper())
    print("")


def run():
  print("Please entre a word")
  word = str(input())

  action = 0
  while(action != 6):
    # Options selection
    print("\nWhat would you like to do with this word?")
    print("[1] Display in a box")
    print("[2] Display lower-case")
    print("[3] Display upper-case")
    print("[4] Display mirrored")
    print("[5] Display repeated")
    print("[6] Quit")
    action = int(input())


    if(action == 1):
      answer = box(word)
      print(answer)
    elif(action == 5):
      answer = reapt_word(word)
      print(answer)
    elif(action == 2):
      answer = lower_case(word)
      print(answer)
    elif(action == 3):
      answer = upper_case(word)
      print(answer)
    elif(action == 4):
      answer = mirrored(word)
    elif(action == 6):
      break
    else:
      print("The entred option is not availble")


run()
