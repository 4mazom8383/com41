print("Please enter a word")
user_word = input()

for position in range(0, len(user_word), 1):
  print(user_word[position])



print("\nWhat strange markings do you see?")
symbols = input()

print("\nIdentifying...\n")

for count in range(0, len(symbols), 1):
  print("index", count, ":", symbols[count])

print("Done!")