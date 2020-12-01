import matplotlib.pyplot as plt
import csv
def data():

  with open('test/csv/train.csv', 'r') as csv_file :

    csv_reader = csv.reader(csv_file)

    # ignore header
    header = next(csv_reader)

    data = {
      'survived':[],
      'sex':[],
      'age':[],
      'fare':[]
    }
    
    for row in csv_reader:
      survived = row[1].strip() 
      #sex = row[1].strip() 
      #age = row[2].strip() 
      #fare = row[3].strip() 


      data['survived'].append(survived)
      #data['sex'].append(sex)
      #data['age'].append(age)
      #data['fare'].append(fare)



  #print(header)
  print()
  return data


def run():
  train = data()
  fig, axs = plt.subplots(1, 1)


  x = range (1, int(train))
  y = train
  axs.plot(x, y)

  labels = ('A', 'B', 'C', 'D')
  sizes = [15, 30, 45, 10]

  plt.pie(sizes, labels=labels)


  plt.tight_layout()
  plt.show()
  
run()