# The Class
class person:

  # Class Attributes 
  # Constant (Once intial value assigned, does not change)
  energy = 100


  # initialiser (special instance method)
  def __init__(self, name, age=0, weight=0):

    # instance attributes  
    self.name = name
    self.age = age
    self.weight = weight
    self.energy = person.energy
      

  def growth(self):
    self.age += 1

  def display(self):
    print(f"{self.name} is {self.age} years old and weighs {self.weight} kg and my energy is {self.energy}")




# the object
prins = person("Prins")
prins = person("Prins", 36)  
prins = person("Prins", 36, 85)    


prins.display()

prins.growth()

prins.display()