import numpy as np

i = open("data/prog505d.txt")
hits = np.array([[]])
bats = np.array([[]])
v=0
for line in i:
  j = line.split(" ")
  print(j[0]+" "+j[1])
  hits = np.stack((hits, [[]]))
  bats = np.concatenate((bats, [[]]))
  for lcv in range(0, len(j)-2, 2):
    hits[v] = np.stack((hits[v], [int(j[lcv+2])]))
    bats[v] = np.concatenate((bats[v], [int(j[lcv+3])]))
    print (f"{int(j[lcv+2])/int(j[lcv+3]):.2f}", end="\t")
  v+=1
  
  print("\n")

print(hits)

for day in range(hits[0].size):
  if day == 0:
    print("Monday:", end=" \t")
  elif day == 1:
    print("Tuesday:", end="\t")
  elif day == 2:
    print("Wednesday:", end="\t")
  elif day == 3:
    print("Thursday:", end="\t")
  elif day == 4:
    print("Friday:", end=" \t")
  elif day == 5:
    print("Saturday:", end="\t")
  else:
    print("Sunday:", end="  \t")

  hit = 0
  bat = 0
  for lcv in range(len(hits)):
    hit += hits[lcv, day]
    bat += bats[lcv, day]
    
  print(hit)