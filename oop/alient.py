from inhabitant import Inhabitant

class Alient(Inhabitant):

  def __int__(self):
    self.technology = []

  def __repr__(self): 
    return f"Alien has:{self.technology}."

  def pickup(self,tech): 
    self.technology.append(tech) 
    
  def drop(self,tech): 
    self.technology.remove(tech)


if (__name__ == "__main__"):
  
  alient = Alient()

  print(repr(alient))
