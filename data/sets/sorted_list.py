def observed():
  observations = []

  for count in range(5):
    print("Please enter an observation:")  
    observation = input()
    observations.append(observation)
  return observations

def remove_observations(observationlist):
  #observed_list = observed()


  is_running = True

  while(is_running):
    print("Do you wish to remove an observation (yes/no)?")
    answer = input()


    #remove an observation
    if (answer == "yes"):
      print(observationlist)
      print("")

      print("What observation do you wish to remove?")
      removed_observation = input()


      #removing syntax
      observationlist.remove(removed_observation)
      print("Done!")
    else:
      is_running =  False  


  #Display the observations
  #print(observed_list)
  #print(len(observed_list))


def run():
  print("Counting observation")
  #remove_observations()

  observations = observed()
  remove_observations(observations)

  observation_set = set()

  #counting observations
  for count in observations:
    data = (count, observations.count(count))
    observation_set.add(data)


  #Displaying oberved list
  for count in observation_set:
    print(f"{count[0]} observed {count[1]} times")
  
run()