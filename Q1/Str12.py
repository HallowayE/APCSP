sentance = input("Sentance: ")
newsent = ""
for i in reversed(range(len(sentance))):
  if sentance[i]==(" "):
    newsent+=sentance[i+1:]
    sentance = sentance[:i]
    newsent+=" "
print(newsent + sentance)
"""
Sentance: Python is pretty cool I guess
guess I cool pretty is Python
"""