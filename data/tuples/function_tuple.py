def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return likelihoods

def run():
  run = likelihood()
  print("Minimum likelihood of falling: {} %".format(min(run)))
  print("Minimum likelihood of falling: {} %".format(max(run)))
  
run()