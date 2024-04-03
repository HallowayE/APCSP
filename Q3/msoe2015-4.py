arr = []
arrdis = []
for i in range(10):
  x=float(input())
  arr.append(x)
  if i >= 2:
    arrsort = arr.copy()
    arrsort.sort()
    arrdis.append(arrsort[len(arr)-3])
print(arr, arrdis)