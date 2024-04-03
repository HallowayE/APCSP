n = int(input("Number of sides: "))
sum = 0
x = []
y = []
x.append(float(input("X0: ")))
y.append(float(input("Y0: ")))
for i in range(1, n):
  x.append(float(input(f"X{i}: ")))
  y.append(float(input(f"Y{i}: ")))
  sum+=(x[i-1]*y[i])-(x[i]*y[i-1])
sum+=(x[len(x)-1]*y[0])-(x[0]*y[len(y)-1])
sum/=-2
print("A =", sum)
