import time

def __lt__(self, other):
  return self.score < other.score

def value(obj):
  return obj.value

class Object:
  def __init__(self, id, value):
    self.id = id
    self.value = value

data = open("data/prog408a.txt")
list  = []

for i in data:
  j=i.split(" ")
  j[1]=j[1].strip()
  obj = Object(j[0], j[1])
  list.append(obj)

# Bubble Sort
print("Bubble Sort")
start = time.perf_counter()
for i in range(1, len(list)):
  for i2 in range(0, len(list)-i):
    if list[i2].value>list[i2+1].value:
      sub = list[i2]
      list[i2]=list[i2+1]
      list[i2+1]=sub
end = time.perf_counter()

for i in list:
  print(i.id + "\t" + i.value)
print(f"{end-start:.8f}")

list.reverse()

# Selection Sort
print("Selection Sort")
start = time.perf_counter()
for i in range(0, len(list)-1):
  min = 99999999
  lcv = 0
  for i2 in range(i, len(list)):
    if int(list[i2].value)<min:
      min = int(list[i2].value)
      lcv = i2
  list[lcv].value=list[i].value
  list[i].value=str(min)

end = time.perf_counter()

for i in list:
  print(i.id + "\t" + i.value)
print(f"{end-start:.8f}")

list.reverse()

#Insertion Sort
print("Insertion Sort")
start = time.perf_counter()
for i in range(1, len(list)):
  i2 = 0
  while (list[i-i2].value>=list[i].value):
    i2+=1
    if i-i2==0:
      break
  list.insert(i-i2, list[i])
  list.pop(i+1)
  
end = time.perf_counter()

for i in list:
  print(i.id + "\t" + i.value)
print(f"{end-start:.8f}")

list.reverse()

#built in sort
print("Built-in Sort")
start = time.perf_counter()
list.sort(key=value)
end = time.perf_counter()
for i in list:
  print(i.id + "\t" + i.value)
print(f"{end-start:.8f}")

list.reverse()

#Suggested Sort
print("Sugested Sort")
start = time.perf_counter()
while len(list)>0:
  min = 999999999
  minid = 0
  for i in list:
    if int(i.value) < min:
      min = int(i.value)
      minid = i
  print(minid.id + "\t" + minid.value)
  list.remove(minid)
end = time.perf_counter()
print(f"{end-start:.8f}")


