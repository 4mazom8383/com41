def search(file_path):
  print("Searching...")
  sections = []
  books = []

  with open(file_path) as file:
    for line in file:
      #Divide stenences starting with section & store them in sections variable
      if line.startswith("Section"):
        parts = line.split(":")
        sections.append(parts[1])
      else:
        books.append(line)

    print("Done!")
    return(sections, books) 

#print and save data
def save(file_path, data):
  print("Saving...")

  with open(file_path, "w") as file:
    file.write(f"Sections: {data[0]}\n")
    #print(f"\nSections: {data[0]}")

    file.write(f"Books: {data[1]}")
   # print(f"Books: {data[1]}\n")
  print("Done!")

#Connecting the two paths Books and Section-Books
def run():
  data = search("data/files/txt2/books.txt")
  save("data/files/txt2/section-books.txt", data)


run()

