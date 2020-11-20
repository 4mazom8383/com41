import matplotlib.pyplot as plt
import csv


first_key = None
second_key = None


def read_data(file_path):
  global first_key, second_key

  with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)


    first_key = header[0].strip()
    second_key = header[1].strip()

    data = {
      first_key:[ ],
      second_key:[ ]
    }

    for row in csv_file:
      data[first_key].append(row[0].strip())
      data[second_key].append(row[1].strip())


    print(data[first_key])
    print(data[second_key])
    #print(data)
    return data

def run():
  data = read_data('visual/subplots/csv_subplots/temps.csv')
  print(data)
  
  fig, axis = plt.subplots(2, 1, sharex='all')
  #x = range(1,8)

  axis[0].plot(data[first_key])
  axis[1].plot(data[second_key])

  plt.tight_layout()
  plt.show()



run()

