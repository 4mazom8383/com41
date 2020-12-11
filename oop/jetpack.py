from tech import tech

class Jetpack(tech):

  def __int__(self):
    super().__int__()

  def __repr__(self):
    return "jetpack()"

  def activate():
    print("Jetpack has been activated")

  def deactivate():
    print("Jetpack has been deactivated")



if (__name__ == "__main__"):
  
  jetpack = Jetpack()

  print(repr(jetpack))