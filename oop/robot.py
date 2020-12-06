class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self, name= 'Robot', age= 10):

    # An instance attribute
    self.name = name
    self.age = age

  # An instance method
  def display(self):
    print(f"I am {self.name} and I am {self.age}")


  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

  def __str__(self):
    return f'Robot {self.name} is {self.age} years old.'

if (__name__ == "__main__"):
  Robot = Robot()
  
  Robot.display()
  print(Robot.laws)

  print(repr(Robot))