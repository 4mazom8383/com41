import matplotlib.pyplot as plt

#x = [0, 5, 10]
#y = [0, 50, 100]

##plt.plot(x, y)
#plt.show()

def display(x, y):
  plt.plot(x, y)
  plt.show()

def run():
  x = [1,2,3,4,5]
  y = [1, 4, 9, 16, 25]

  display(x, y)

run()