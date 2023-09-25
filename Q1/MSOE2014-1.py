def main():
  word = input("Enter a word: ")
  word = word.lower()
  dblcnt = 0
  for lcv in range(0, len(word)-1):
    if word[lcv]==word[lcv+1]:
      dblcnt+=1
  print(f"The word '{word}' contains {dblcnt} double letters")
  pass


if __name__ == "__main__":
  main()