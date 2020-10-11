print("How many bars should be charged?")
charge = int(input())

Charging = 0
# Display the current count    
while (Charging < charge):

  # Update the current iteration count
  Charging = Charging + 1

  print("Charging:", "█"  * Charging)

print("The battery is fully charged.")

