
def linear_search(list, target):
  for i in range(0, len(list)):
    if list[i]==target:
      return i
  return -1

def  binary_search(list, target):
  list.sort()
  check = len(list)/2
  if check==target:
    return check
  if check>target:
    return binary_search(list[check:len(list)], target)
  if check<target:
    return binary_search(list[0:check], target)
  return -1

data = open("data/prog408b.dat")

t = input("Enter a number")

print(linear_search(data, t))
print(linear_search(data.sort(), t))
print(linear_search(data, t))

