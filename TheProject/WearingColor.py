def perColor(students, length, color):
  cnt = 0
  for i in students:
    if i[1].upper()==color.upper() or i[2].upper()==color.upper() or i[3].upper()==color.upper():
      cnt+=1
  return (float(cnt)/float(length))*100

def mostColor(student, length, color):
  num = []
  max = 0
  most = []
  for i in range(length):
    num.append(0)
    if student[i][1].upper()==color.upper():
      num[i]+=1
    if student[i][2].upper()==color.upper():
      num[i]+=1
    if student[i][3].upper()==color.upper():
      num[i]+=1
    if num[i]>max:
      max=num[i]
  for i in range(len(num)):
    if num[i] == max:
      most.append(student[i][0])

  ret = ""
  
  for i in most:
    ret+= i+", "
  return ret.strip(", ")

students = []

numP = int(input("How many people: "))
for i in range(numP):
  
  stuName = input(f"Student {i+1}'s name: ")
  stuShirt = input(f"Student {i+1}'s shirt color: ")
  stuPants = input(f"Student {i+1}'s pants color: ")
  stuOther = input(f"Student {i+1}'s pants color: ")
  students.append((stuName, stuShirt, stuPants, stuOther))

color = input("What color would you like to know the percentage of? ")

percent = perColor(students, numP, color)

print(f"Percentage of people wearing {color}: %.2f%%" % percent)
print(f"Person(s) with the most {color}: ", mostColor(students, numP, color))



    