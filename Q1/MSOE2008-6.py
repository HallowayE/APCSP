seq = input("Enter sequence: ")
target = input("Enter target: ")
cnt = 0
while target in seq:
  cnt+=1
  seq=seq[seq.index(target)+1:]
print(cnt)
"""
Enter sequence: CGATTACGCGACGAT
Enter target: CGA
3
"""