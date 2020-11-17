import matplotlib.pyplot as plt

def read_data(file_path):
  temps = []

  with open ('visual/subplots/temps.txt') as file:
    
    for line in file:
      temp = int(line.strip())
      temps.append(temp)
      #print(temps)
  return temps


def run():
  data = read_data('visual/subplots/temps.txt')

  fig, axs = plt.subplots(1, 2)

  x = range(1,8)
  y = data

  axs[0].plot(x, y)
  axs[1].bar(x, y)



  plt.tight_layout()
  plt.show()

run()