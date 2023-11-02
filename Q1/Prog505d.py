import numpy as np

i = open("data/prog505d.txt")
hits = [[]]
bats = [[]]
v=0
players=0
for line in i:
  players+=1
  j = line.split(" ")
  print(j[0]+" "+j[1])
  hits.extend([[]])
  bats.extend([[]])
  for lcv in range(0, len(j)-2, 2):
    hits[v].extend([int(j[lcv+2])])
    bats[v].extend([int(j[lcv+3])])
    print (f"{int(j[lcv+2])/int(j[lcv+3]):.2f}", end="\t")
  v+=1
  
  print("\n")

tothit=0
for day in range(len(hits[0])):
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
  for lcv in range(len(hits)-1):
    hit += hits[lcv][day]
    bat += bats[lcv][day]
  print(hit, f"\t{hit/bat:.2f}")
  tothit+=hit
  
print(f"Total hits:\t{tothit}")
"""
Fred Sluggo
0.50    0.25    0.33    0.25    0.00    0.00    1.00

Lydia Crusher
0.67    0.67    0.80    0.40    0.25    1.00    0.25

Braeden Boomer
1.00    0.50    0.62    0.50    0.20    0.33    0.00

Noah Niller
0.33    0.57    0.33    0.75    0.50    0.33    0.29

Ruben Romper
0.00    0.33    0.50    0.40    0.29    0.38    0.00

Lisa Longball
1.00    0.50    0.71    0.25    0.75    0.50    0.20

Claire Corner
0.25    0.67    0.38    0.44    0.80    0.33    0.20

Jared Just
1.00    0.50    0.40    0.29    0.12    1.00    0.33

Monday:     8   0.47
Tuesday:    19  0.51
Wednesday:  24  0.52
Thursday:   19  0.40
Friday:     16  0.36
Saturday:   15  0.39
Sunday:     12  0.32
Total hits: 113
"""
  