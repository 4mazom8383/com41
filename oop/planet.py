from human import Human
from robot import Robot

class Planet:

  # An initialiser (special instance method)
  def __init__(self):
    # An instance attribute as empty list
    self.inhabitants = []

    

  def __repr__(self):
    return f"planet(inhabitants={self.inhabitants}"

  def __str__(self):
    return f"This planet has {len(self.inhabitants)} inhabitants"



  # Add
  def add(self, inhabitant):
    self.inhabitants.append(inhabitant)

  # Remove
  def remove(self, inhabitant):
    self.inhabitants.remove(inhabitant)




if (__name__ == "__main__"):
  planet = Planet()

  print(repr(planet))

  planet.add("prins")

  print(repr(planet))

  print(planet)