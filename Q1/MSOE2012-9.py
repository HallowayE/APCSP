numeral = input("Numeral: ")
decimal = 0
for lcv in numeral:
  if lcv=="M":
    decimal+=1000
  elif lcv =="D":
    decimal+=500
  elif lcv =="C":
    decimal+=100
  elif lcv =="L":
    decimal+=50
  elif lcv =="X":
    decimal+=10
  elif lcv =="V":
    decimal+=5
  else:
    decimal+=1
print ("Decimal:", decimal)
"""
Numeral: MCCLXXIII
Decimal: 1273
"""