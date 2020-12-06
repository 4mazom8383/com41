class Planet:

  # An initialiser (special instance method)
  def __init__(self):
    # An instance attribute
    self.humans = "Robot"
    self.robot = 40

    
  # An instance method
  def display(self):
    print(f"I am {self.name} and I am {self.age}")