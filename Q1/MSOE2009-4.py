import math

a = int(input("a="))
b = int(input("b="))
n = int(input("number of boxes ="))
def f(x):
  return math.exp(-x*x/2)/math.sqrt(2*math.pi)

h = int((b-a)/n)
area = 0
for lcv in range(a, b+h, h):
  area+=f(a + lcv-a)
area*=h
print (area)
"""
a=1
b=70
number of boxes =10
1.4518243471696686
"""