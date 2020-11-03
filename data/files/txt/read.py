def search(filepath):
  print("Searching...")
  with open(filepath) as file:
    data = file.read()
    print(data)

  print("")
  print("")
  print("")

  with open(filepath) as file:
    for line in file:
      print(f"Looked in {line}", end= "")


  print("Done!")


def run():
  search("data/files/txt/data.txt")


run()