print("What's your name?")
name = str(input())

print("How old are you (in years)?")
age = int(input())


print("How tall are you (in meters)?")
height = float(input())
#print("Your height is",float (height))

print("How much do you weigh (in kilograms)?")
weight = float(input())
#print("Your weigh is",float (weigh))

bmi = weight / (height ** 2)

print(str(name), "you're", int (age), "years old and your bmi is{:.2f} ".format(bmi))