def countWordsFromFile():
  file = input('File name:')
  f = open(file, 'r')
  wordCount = 0
  letterCount = 0
  for l in f:
    words = l.split()
    wordCount = wordCount+len(words)
    for i in l.split():
      letterCount += len(i)

  print(wordCount)
  print(letterCount)
countWordsFromFile()