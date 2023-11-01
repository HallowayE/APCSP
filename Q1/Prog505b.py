

def ave(arr):
  cnt = 0
  for line in arr:
    cnt+=int(line)
  cnt/=len(arr)
  return cnt

def grade(n):
  num=int(n)
  g = ""
  if num>=90:
    g="A"
  elif num>=80:
    g="B"
  elif num>=70:
    g="C"
  elif num>=60:
    g="D"
  else:
    g="F"
  return g

arr = []
nums =[[]]
i = open("data/prog505b.txt")
arnum = 0
grades = []
for line in i: 
  line=(line.strip("\n"))
  if line.isalpha():
    if len(arr)!=0:
      average = ave(arr)
      grad = grade(average)
      grades.append(grad)
      print(f"\t\t{average}\t{grad}\n")
      arr=[]
      nums.append([])
      arnum+=1
    print(line, end=" ")
  else:
    nums[arnum].append(line)
    arr.append(line)
    print(f"\t{line}", end="")
average = ave(arr)
grad = grade(average)
grades.append(grad)
print(f"\t\t{average}\t{grad}\n")


for lcv in range(len(nums[0])):
  if lcv == 0:
    let = "A"
  elif lcv ==1:
    let = "B"
  elif lcv ==2:
    let = "C"
  elif lcv == 3:
    let = "D"
  else:
    let = "F"
  print("Test", lcv, end="\t")
  test=[]
  for lcv2 in nums:
    test.append(lcv2[lcv])
  
  print(f"{ave(test):.2f}\t\t\t{let} {grades.count(let)}")


"""
Sam Lilly   80  77  82  86  90      83.0    B

Fred Biggie     70  72  88  90  93      82.6    B

Sally Awesome   92  91  85  99  93      92.0    A

Test 0  80.67           A 1
Test 1  80.00           B 2
Test 2  85.00           C 0
Test 3  91.67           D 0
Test 4  92.00           F 0
"""