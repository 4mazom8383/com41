from planet import Planet
from robot import Robot
from human import Human
import matplotlib.pyplot as plt

import random

# Class called Universe
class Universe:

  def __init__(self):
    self.planets = []

  def __repr__(self):
    return f"universe(planets={self.planets})"

  def __str__(self):
    return f"The universe contains {len(self.planets)} planets."


  # instance method
  def generate(self):
    # create a new planet
    planet = Planet()

    # populate with random humans and robots
    for index in range(random.randint(1, 5)):
      robot = Robot(f"Robot{index}")
      planet.add(robot)

    for index in range(random.randint(1, 5)):
      human = Human(f"Human{index}")
      planet.add(human)

    # add to list of planets
    self.planets.append(planet)

  def show_populations(self):
    num_subplots = len(self.planets)
    
    fig, axs = plt.subplots(1, num_subplots)
    
    for index in range(num_subplots):
      planet = self.planets[index]

      num_humans = 0
      num_robots = 0

      for inhabitant in planet.inhabitants:
        if isinstance(inhabitant, Human):
          num_humans += 1
        elif isinstance(inhabitant, Robot):
          num_robots += 1

      print(num_humans)
      print(num_robots)

      ax = fig.add_subplot(1, num_subplots, index+1)
      ax.bar([1,2], [num_humans,num_robots])
      

    plt.tight_layout()  
    plt.show()


if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.show_populations()