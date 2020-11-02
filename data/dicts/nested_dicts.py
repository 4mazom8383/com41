def short_pattern():
  pattern = {
    "sequence":{"Cake":"101", "occurrences":5}
  }
  return pattern

def medium_pattern():
  pattern = {
    "sequence":{"Cake":"111000", "occurrences":25}
  }
  return pattern

def long_pattern():
  pattern = {
    "sequence":{"Cake":"1100110011001100", "occurrences":50}
  }
  return pattern

def run():
  print("Analysing patterns...")
  #Restore in a new dictionary
  patterns = {
    "short sequence":short_pattern(),
    "medium sequence":medium_pattern(),
    "long sequence":long_pattern()
  }

  #Display dictionary content using items method
  for key, value in patterns.items():
    print(f"{key}: {value}")

run()