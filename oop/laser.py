from tech import tech

class Laser(tech):

  MAX_RANGE = 100


  def __int__(self):
    super().__int__()

  def activate():
    print("Laser has been activated")


  def deactivate():
    print("Laser has been deactivated")

  def fire(range_distance): 
    if(range > Laser.MAX_RANGE): 
      print(f"Fired maximum raneg of {Laser.MAX_RANGE}")
    else:
      print(f"Fired a distance of {range_distance}")


if (__name__ == "__main__"):
  
  laser = Laser()

  print(repr(laser))

