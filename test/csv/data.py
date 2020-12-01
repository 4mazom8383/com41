import matplotlib.pyplot as plt
import csv
def data():

  with open('test/csv/data.csv') as csv_file:

    csv_reader = csv.reader(csv_file)


    # ignore header
    header = next(csv_reader)


    data = {
      'sex':[],
      'age' : []
    }

    for row in csv_reader:
      sex = row[0].strip() 
      age = row[1].strip() 


      data['sex'].append(sex)
      data['age'].append(int(age))

    return data

def run():
  datas = data()
  print(datas)
  fig, axs = plt.subplots(4, 1)


  # Pie Chart
  male = datas['sex'].count("male")
  female = datas['sex'].count("female")
  labels = ('Male', 'Female')
  sizes = [male, female]
  axs[0].pie(sizes, labels=labels,startangle=90)


  # Historgram
  axs[1].set_ylabel('Number of Ages')
  axs[1].set_xlabel('Ages')
  axs[1].set_title('Scores by group and gender')

  axs[1].hist(datas['age'])
  axs[1].grid()


  year = datas['age']  
  tutorial_public = datas['age']
  #tutorial_premium = [0, 0, 13, 56, 39, 14]  
  axs[2].plot(year, tutorial_public)
  #axs[2].plot(year, tutorial_premium)

  #axs[2].xlabel('Year')  
  #axs[2].ylabel('Number of futurestud.io Tutorials')




  labels = ['22', '24', '26', '28', '30']
  men_means = [20, 35, 30, 35, 27]
  #women_means = [25, 32, 34, 20, 25]
  men_std = [2, 3, 4, 1, 2]
  #women_std = [3, 5, 2, 3, 3]
  #width = 0.35# the width of the bars: can also be len(x) sequence

  axs[3].bar(labels, men_means,yerr=men_std, label='Men')
  #axs[3].bar(labels, women_means, width, yerr=women_std, bottom=men_means,label='Women')


  #axs[3].legend()
  axs[3].grid()








  plt.grid()
  plt.tight_layout()
  plt.show()



run()