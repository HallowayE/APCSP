def set(x):
  x=(x*(x+1)/2)
  return int(x)

num = int(input("enter the number: "))

x = 0
T = set(x)
o=0
t=0
th=0
sum = 0

while T<num:
  x+=1
  T = set(x)
x-=1
T = set(x)

for i in range(x+1, -1, -1):
  o = set(i)
  for i2 in range(i, -1, -1):
    t = set(i2)
    if t < 0:
      break
    for i3 in range(i2, -1, -1):
      th = set(i3)
      if th<0:
        break
      sum = o+t+th
      if sum == num:
        print(o, t, th)