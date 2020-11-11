import matplotlib.pyplot as plt

def data():
  paths = {}

  print("What type of line they would like (:, -- or -)")
  the_type = input()


  print("What colour they would like (r, g, b)")
  color = input()


  print("What style of marker they would like (c, s or ^)")
  style = input()
  #storing the line style, colour, marker style in the dictionary as key-value pairs

  paths['color'] = color
  paths['style'] = style
  paths['the_type'] = the_type
  
  #paths = {"type", types,"color", color,"style", style}
  
  return paths


def generate():
  print("How many lines would you like to display?")
  lines_numbers = int(input())

  for p in range (lines_numbers):
    # Calling first function & store it in a variable named the_data.
    the_data = data()

    #Display a line graph using the values stored in the_data and random values for x and y
    x = [1,2,3,4,5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y, f"{the_data['color']}{the_data['style']}{the_data['the_type']}")

  plt.show()

def run():
  print("Running....")
  generate()

  print("Done!")


run()