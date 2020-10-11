print("What phrase do you see?")
phrase = str(input())

print("\nReversing...\n")

for count in range(len(phrase) - 1, -1, -1):
  print(phrase[count], end="")

