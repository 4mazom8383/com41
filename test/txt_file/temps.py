import matplotlib.pyplot as plt

def data(file_path):
  
  data = [ ]
  
  with open (file_path) as file:
    
    
    for row in file:
      temp = row.strip()
      data.append(temp)
  

  return data
  
  
def run():
  temps = data('test/txt_file/temps.txt')
  fig, axs = plt.subplots(1, 2)

  x = range(1,8)
  y = temps

  axs[0].plot(x, y)
  axs[1].bar(x, y)



  plt.tight_layout()
  plt.show()
  
run()