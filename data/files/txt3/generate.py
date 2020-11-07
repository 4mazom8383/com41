def search(file_name):
  print("Searching...")
  data = {}

  with open(file_name) as file:
    section = ""
    for line in file:
      #Dived the sentence to 2 sections
      if line.startswith("Section"):
        section = line.split(":")[1][:-1]

      #Add the second section to the empthy variable
      elif (section in data):
        data[section].append(line[:-1])
        
      # Add the remaining list to variable section
      # The list that not start with "Section"  
      else:
        data[section] = [line[:-1]]
        #data[section].append(line[:-1])


    print("Done!")
    #print(data)
    return data 
def run():
  #List items path 
  data = search("data/files/txt3/books.txt")

  #The new file to write the list
  with open("data/files/txt3/generated.csv", "w") as file:
    #Method 1 to write in the new file
    for section, books in data.items():
      for book in books:
        file.write(f"{section},{book}\n")

    #Method 1 to write in the new file
    #for item in data.items():
      #section = item[0]
      #books = item[1]
      
run()  
#search("data/files/txt3/books.txt")