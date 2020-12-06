class Human:
  # Constant (Once intial value assigned, does not change)
  energy = 100

  # A class attribute
  #laws = "Protect, Obey and Survive"

  # A class method
  #def the_laws():
  #  print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Human"
    self.age = 0
    self.energy = Human.energy

  # An instance method
  def display(self):
    print(f"I am {self.name} and I am {self.age} and my energy is {self.energy}")

  def growth(self):
    self.age += 1


if (__name__ == "__main__"):
  Human = Human()

  Human.growth()

  Human.display()



  
