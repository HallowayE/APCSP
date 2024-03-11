class Pet:
  def __init__(self, name, cute, nice, fluff):
    self.name = name
    self.cute = int(cute)
    self.nice = int(nice)
    self.fluff = int(fluff)

  def __str__(self):
    return f"{self.name}: cute = {self.cute}, nice = {self.nice}, fluff = {self.fluff}"

i = open("Project3/Pets.txt")

pets = []

for line in i:
  pet = line.split()
  pet.pop(1)
  pet.pop(2)
  pet.pop(3)
  pets.append(Pet(pet[0], pet[1], pet[2], pet[3]))
  
myCute = int(input("What is your ideal cutness? "))
myNice = int(input("What is your ideal niceness? "))
myFluff = int(input("What is your ideal fluffiness? "))

cH = 10000
index = 0

for i in range(len(pets)):
  hyp = pow(pow(pets[i].cute-myCute, 2)+pow(pets[i].nice-myNice, 2)+pow(pets[i].fluff-myFluff, 2), 0.5)
  if hyp<cH:
    cH = hyp
    index = i

print(pets[index])
