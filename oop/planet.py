from human import Human
from robot import Robot

class Planet:

  # An initialiser (special instance method)
  def __init__(self):
    # An instance attribute as empty list
    self.inhabitants = {
      'humans':[],
      'robots':[]
    }

    

  def __repr__(self):
    return f"planet(humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']})"

  def __str__(self):
    return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots."



  # Add
  def add_human(self, human):
    self.inhabitants['humans'].append(human)

  def add_robot(self, robot):
    self.inhabitants['robots'].append(robot)


  # Remove
  def remove_human(self, human):
    self.inhabitants['humans'].remove(human)

  def remove_robot(self, robot):
    self.inhabitants['robots'].remove(robot)


if (__name__ == "__main__"):
  planet = Planet()
  print(repr(planet))
  planet.add_human(prins)
  print(repr(planet))
  print(planet)