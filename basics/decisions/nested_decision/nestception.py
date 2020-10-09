print("Where should I look?")
where = input()


#Block 1
if(where == "in the bedroom"):
  print("Where in the bedroom should I look?")
  where_bedroom = input()

  if(where_bedroom == "under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery.")

#Block 2
elif(where == "in the bathroom"):
  print("Where in the bathroom should I look?")
  where_bedroom = input()
  
  if(where_bedroom == "in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery.")

#Block 3
elif(where == "in the lab"):
  print("Where in the lab should I look?")
  where_bedroom = input()
  
  if(where_bedroom == "on the table"):
    print("Yes! I found my battery!")
  else:
    print("Found some tools but no battery.")

#Otherwise
else:
  print("I do not know where that is but I will keep looking.")