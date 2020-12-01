import matplotlib.pyplot as plt



def combined():



  fig, axs = plt.subplots(1, 1)

  x1 =   [ 3,5,7]

  y1 =   [ 3,5,3] 



  x2 =   [ 3,5,7]

  y2 =   [ 5,3,5] 



  x3 =   [ 3,3,7]

  y3 =   [ 3,5,4]



  x4 =   [ 7,7,3]

  y4 =   [ 3,5,4] 





  axs.plot(x1, y1, 'ro')

  axs.plot(x2, y2, 'bo:')

  axs.plot(x3, y3, 'go--')

  axs.plot(x4, y4, 'yo--')



def run():

  combined()

  plt.show()





run()





