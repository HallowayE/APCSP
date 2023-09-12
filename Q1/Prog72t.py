num1 = int(input("Enter the first time: "))
num2 = int(input("Enter the second time: "))

hour1 = int(num1/100)
min1 = num1%100
hour2 = int(num2/100)
min2 = num2%100

if (num2>num1):
  hours = hour2-hour1
  mins = min2-min1
else:
  hours = 24-hour1+hour2
  mins = min1-min2

print (hours, "hours", mins, "minutes")

"""
Enter the first time: 900
Enter the second time: 1730
8 hours 30 minutes
"""

  