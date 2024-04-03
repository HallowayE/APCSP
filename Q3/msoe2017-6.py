def dede(n):
  prime = []
  
  for num in range(1, n+1):
    if num > 1:
     for i in range(2,num):
         if (num % i) == 0:
             break
     else:
         prime.append(num)
      
  factor=[]
  for i in prime:
    if n%i==0:
      factor.append(i)

  de = n
  for i in factor:
    de*=(1+(1/i))
  print(de)

num = int(input("num: "))
dede(num)
    