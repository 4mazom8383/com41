import matplotlib.pyplot as plt
import csv
def read_data():

  with open('visual/subplots/titanic/train.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    data = {
      'survived':[],
      'sex':[],
      'age':[],
      'fare':[]
    }
    
    for row in csv_reader:
      survived = row[0].strip() 
      sex = row[1].strip() 
      age = row[2].strip() 
      fare = row[3].strip() 


      data['survived'].append(survived)
      data['sex'].append(sex)
      data['age'].append(age)
      data['fare'].append(fare)



    #print(data)
    return data

def run():
  data = read_data()
  #print(data)
  
  fig, axs = plt.subplots(4, 1)
  
  axs[0].plot(data['survived'])
  axs[1].bar(data['sex'], data['sex'])
  axs[2].bar(data['age'], data['age'])
  axs[3].plot(data['fare'])

  plt.tight_layout()
  plt.show()



run()