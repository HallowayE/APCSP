copies = int(input("Number of copies: "))
priceper = 0

if copies<=99:
  priceper=0.3
elif copies <=499:
  priceper = 0.28
elif copies<=749:
  priceper = 0.27
elif copies <=1000:
  priceper = 0.26
else:
  priceper = 0.25

price = copies * priceper
print("price:", price)

"""
Number of copies: 1001
price: 250.25
"""