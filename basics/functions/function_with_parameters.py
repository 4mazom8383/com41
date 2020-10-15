def climb_ladder(remaining_steps,crossed_steps):

  if(remaining_steps > crossed_steps):
    print("Still some way to go!")
  else:
    print("We are almost there!")
    

climb_ladder(5, 2)
climb_ladder(2, 5)