weight = int(input("Enter package weight in killograms: "))
length = int(input("Enter package length in centimeters: "))
width = int(input("Enter package width in centimeters: "))
height = int(input("Enter package heigth in centimeters: "))

size = length*width*height

if weight > 27 and size > 100000:
  print("Too heavy and too large")
elif weight > 27:
  print("Too heavy")
elif size > 100000:
  print("Too large")
else:
  print("All good")

"""
Enter package weight in killograms: 32
Enter package length in centimeters: 10
Enter package width in centimeters: 25
Enter package heigth in centimeters: 38
Too heavy
"""