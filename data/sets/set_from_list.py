def observed():
  observations = []
  for count in range(3):
    #print("Please entre values")
    observation = input()
    observations.append(observation)
  return observations


def run():
  print("Counting observation")
  observations = observed()
  observations_set = set()

  for observation in observations:
    observations_set.add((observation, observations.count(observation)))
    #print(observations_set)
    #print((observation, observations.count(observation)))
  print(observations_set)
run()


#user_web_browsers = ["Chrome", "Firefox", "Chrome", "Firefox", "Edge", "Firefox"]
#print(user_web_browsers)
#user_web_browsers.add("Opera")


##list_of_web_browsers = user_web_browsers
#list_of_web_browsers.add("Opera")
#list_of_web_browsers.append("Opera")
#print(list_of_web_browsers)

#user_web_browsers.add("Opera")


