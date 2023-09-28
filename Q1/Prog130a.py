num = int(input("Enter a number: "))
cnt = 0
while num!=1:
  prev = num
  if num%2==0:
    num=int(num/2)
    print(prev, "is even, so I take half = ", num)
  else:
    num=(3*num)+1
    print(prev, "is od, so I make 3n+1 = ", num)
  cnt+=1
print("the process took ", cnt, "steps to reach 1")
"""
Enter a number: 17
17 is od, so I make 3n+1 =  52
52 is even, so I take half =  26
26 is even, so I take half =  13
13 is od, so I make 3n+1 =  40
40 is even, so I take half =  20
20 is even, so I take half =  10
10 is even, so I take half =  5
5 is od, so I make 3n+1 =  16
16 is even, so I take half =  8
8 is even, so I take half =  4
4 is even, so I take half =  2
2 is even, so I take half =  1
the process took  12 steps to reach 1
"""