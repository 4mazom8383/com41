import matplotlib.pyplot as plt   
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

def animate(frame_number):
  global ax
  ax.set_xlim(0,720)
  ax.set_ylim(-1,1)

  #NumPy array named x with a range from 0 to the current frame number.
  x_in_degrees = np.arange(0, frame_number)


  #Calculate the y values by multiplying the x values by PI/180 and then find the sine of the result (i.e. sine of (x * PI/180)).
  x_in_radians = x_in_degrees * (np.pi / 180)

  # Store the y value on Y varible
  y = np.sin(x_in_radians)

  
  # plot the points given be x and y.
  ax.plot(x_in_degrees, y)



  # Adding Titles and Grid
  ax.set(xlabel='Just a Title', ylabel='Just a Title',
       title='Just a Title')
  ax.grid()   



def run():


  global line
  sine_animation = animation.FuncAnimation( 
    fig, 
    animate, 
    frames = 720, 
    interval = 100
  )
  plt.show()

run()

