eggs = int(input("Number of eggs purchased: "))

dozen = eggs/12

price = 0.0

if dozen <4:
  price=0.50
elif dozen < 6:
  price = 0.45
elif dozen < 11:
  price = 0.40
else:
  price = 0.39

bill = eggs*(price/12)

print("$",bill)

"""
Number of eggs purchased: 18
$ 0.75
"""