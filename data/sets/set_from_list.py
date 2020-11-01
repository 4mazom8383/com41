def observed():
  observations = []
  print("Please entre 4 values")
  for count in range(4):
    observation = input()
    observations.append(observation)
  return observations


def run():
  print("Counting observation")
  observations = observed()

  observations_set = set()

  for observation in observations:
    #observations_set.add((observation, observations.count(observation)))


    #Count how many times the value is been observed
    occurrences = observations.count(observation)
    observations_set.add((observation, occurrences))

  
  # TUPLE #Display the value and how many times 
  for count in observations_set:
    print(f"{count[0]} observed {count[1]} times.")


  

run()


#user_web_browsers = ["Chrome", "Firefox", "Chrome", "Firefox", "Edge", "Firefox"]
#print(user_web_browsers)
#user_web_browsers.add("Opera")


##list_of_web_browsers = user_web_browsers
#list_of_web_browsers.add("Opera")
#list_of_web_browsers.append("Opera")
#print(list_of_web_browsers)

#user_web_browsers.add("Opera")


