import matplotlib.pyplot as plt   
import matplotlib.animation as animation
     
fig, ax = plt.subplots()
    
def animate(frame):    
  # your code here
  #Cla.() to show only one circle
  #ax.cla()
  ax.set_xlim(0,20)
  ax.set_ylim(0,20)
  ax.plot(frame,frame, 'ro')
     
def run():
  #global fig  
  simple_animation = animation.FuncAnimation(fig, animate, frames = 20, interval = 1000, repeat = False)

  plt.show()
      
run()