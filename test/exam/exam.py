import matplotlib.pyplot as plt

def separated():

  fig, axs = plt.subplots(2, 2)

  x1 = [3,7,5,3]
  y1 = [3,3,5,3] 

  axs[0].plot(x1, y1, 'ro:--')


  x2 = [5,7,3,5]
  y2 = [3,5,5,3] 
  axs[1].plot(x2, y2, 'bs:')


  x3 = [3,7,3,3]
  y3 = [3,4,5,3]
  axs[2].plot(x3, y3, 'g-.*')

  x4 =[3,7,7,3]
  y4 =[4,3,5,4] 
  axs[3].plot(x4, y4, 'yp-')


def run():
  separated()
  plt.show()

run()
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