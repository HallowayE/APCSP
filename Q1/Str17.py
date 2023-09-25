sentance = input("Sentance: ")
sentance = sentance.lower()
max = 0
fChar = ""
for lcv in range(len(sentance)):
  cnt = 0
  char = sentance[lcv]
  for lcv2 in range(len(sentance)):
    if sentance[lcv2] == char:
      cnt+=1
      if cnt>max:
        max=cnt
        fChar=char
print (fChar)
"""
Sentance: antidisestablishmentarianism
i
"""