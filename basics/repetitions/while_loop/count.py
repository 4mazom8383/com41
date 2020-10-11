print("How many live cables should I avoid?")
cables_to_avoid = int(input())

avoided_cables = 0
# Display the current count    
while (avoided_cables < cables_to_avoid):

  # Update the current iteration count
  avoided_cables = avoided_cables + 1
  print("Avoiding....", end="")
  print("Done!", avoided_cables ,"live cables avoided.")


print("All live cables have been avoided.")

