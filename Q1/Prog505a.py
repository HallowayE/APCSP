def points(books):
  p=0
  for lcv in range(0, books):
    if lcv<3:
      p+=10
    elif lcv < 6:
      p+=15
    else:
      p+=20
  return p
print ("Reading contest\n")
print ("Name\t\t\tBooks\tPoints")
i = open("data/prog505a.txt")
for line in i:
  j = line.split(" ")
  name = j[0]+" "+j[1]
  book = int(j[2])
  point = points(book)
  print(f"{name}  \t{book}\t\t{point}")

"""
Reading contest

Name            Books   Points
Sam Summer      4       45
Linda Lazy      2       20
Paul Prodder    5       60
K.C. Master     8       115
Richie Reader   6       75
"""