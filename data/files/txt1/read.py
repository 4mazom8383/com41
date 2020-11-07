def search(filepath):
  print("Searching...")
  #Display the content using read() function
  with open(filepath) as file:
    data = file.read()
    print(data)

  print("")
  print("")
  print("")

  #Display the content using a For loop
  with open(filepath) as file:
    for line in file:
      print(f"Looked in {line}", end= "")
  print("\n...Done!")


def run():
  search("data/files/txt1/data.txt")


run()