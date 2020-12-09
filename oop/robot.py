from inhabitant import Inhabitant
class Robot(Inhabitant):



  # initialiser
  def __init__(self, name="Robot", age=0):
    super().__init__ (name,age)

  # magic methods
  def __repr__(self):
    return f'Robot(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

  # instance methods
  def display(self):
    print(f"I am {self.name}")


if (__name__ == "__main__"):
  
  Robot = Robot()
  print(repr(Robot))
  Robot.eat(99)
  
  
  print(repr(Robot))
  Robot.move(10)
  print(repr(Robot))
  Robot.eat(5)
  print(repr(Robot))
  Robot.eat(20)
  print(repr(Robot))