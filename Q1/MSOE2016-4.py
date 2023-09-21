n = int(input("φ"))
cnt=0
factors = []


for i in range(1, n):
  cont = True
  if i == 1:
    cnt+=1
  elif n%i==0:
    factors.append(i)
  else:
    for factor in factors:
      if i%factor==0:
        cont=False
    if cont:
      cnt+=1
print(cnt)

"""
φ1500
400
"""