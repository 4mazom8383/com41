def steps():
  likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
  return likelihoods

def run():
  #Storing steps function in a new variable 
  all_steps = steps()

  #Empty lists
  good_steps = []
  bad_steps = []

  for step in all_steps:
    if (step[1] >= 50):
      #Adding Step to the empthy list bad_steps
      bad_steps.append(step)
      print(step)
    else:
      #Adding Step to the empthy list good_steps
      good_steps.append(step) 

  print("")

  print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")
  #print({len(good_steps)})
  print("")
  print(good_steps)
  print(bad_steps)
run()