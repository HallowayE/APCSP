a6 = -0.09
a5 = 1.6108
a4 = -10.9167
a3 = 34.7625
a2 = -52.0433
a1 = 31.1767
a0 = -4

def f(x):
  return (a6 * pow(x, 6)) + (a5 * pow(x, 5)) + (a4 *
  pow(x, 4)) + (a3 * pow(x, 3)) + (a2 * pow(x, 2)) + (a1 * x) + a0

def fprime(x):
  return (6* a6 * pow(x, 5)) + (5 * a5 * pow(x, 4)) + (5 * a4
  * pow(x, 3)) + (3 * a3 * pow(x, 2)) + (2 * a2 * x) + a1

n = float(input("x value: "))
print(f"Initial position: f({n}) = {f(n):.5f}")

while abs(f(n))>=0.001:
  n-=(f(n)/fprime(n)*180)
  print(f"Refined zero: f({n:.5f}) = {f(n):.5f}")
"""
x value: 4
Initial position: f(4.0) = -1.04200
Refined zero: f(3.73246) = -0.28317
Refined zero: f(3.64315) = -0.00588
Refined zero: f(3.64116) = 0.00028
"""