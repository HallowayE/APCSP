def isprime(num):
  for i in range(num-1, 1, -1):
    if num%i==0:
      return False
  return True

n = int(input("Enter a number: "))
if isprime(n):
  print("Prime")
else:
  print("Not prime")