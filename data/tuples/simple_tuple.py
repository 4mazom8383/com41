temperatures = (19, 23, 21, 21, 20, 18, 22)

# Concatenate tuples (this creates a new tuple)
all_temperatures = temperatures + (20, 21)
print(all_temperatures)

# Repeat a tuple
print(temperatures * 2)

# Check membership of a tuple
print(20 in temperatures)


print("The lowest temperature is: {}".format(min(temperatures)))
print("The highest temperature is: {}".format(max(temperatures)))


def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return likelihoods

def run():
  run = likelihood()
  print("Minimum likelihood of falling: {} %".format(min(run)))
  
run()