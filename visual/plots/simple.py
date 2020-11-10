import matplotlib.pyplot as plt

#x = [0, 5, 10]
#y = [0, 50, 100]

##plt.plot(x, y)
#plt.show()

def display(x, y):
  #plt.plot(x, y)#solid line
  #plt.plot(x, y, 'o')   # will display circle markers
  #plt.plot(x, y, 's')   # will display square markers
  #plt.plot(x, y, 'o-')  # will display circle markers with a solid line
  #plt.plot(x, y, 'o--') # will display circle markers with a dashed line
  #plt.plot(x, y, 'o:')  # will display circle markers with a dotted line
  #plt.plot(x, y, 'yo')   # will display yellow markers
  plt.plot(x, y, 'ro--') # will display a red dashed line
  plt.show()

def run():
  x = [1,2,3,4,5]
  y = [1, 4, 9, 16, 25]

  display(x, y)

run()