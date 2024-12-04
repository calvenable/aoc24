# Advent of Code 2025 - day04

def countXmas(x, y, wordsearch):
  if (wordsearch[x][y] != 'X'):
    return 0
  
  count = 0
  if (x >= len('XMAS')-1 and y >= len('XMAS')-1):
    if (wordsearch[x-1][y-1] == 'M' and wordsearch[x-2][y-2] == 'A' and wordsearch[x-3][y-3] == 'S'):
      count += 1

  if (x >= len('XMAS')-1):
    if (wordsearch[x-1][y] == 'M' and wordsearch[x-2][y] == 'A' and wordsearch[x-3][y] == 'S'):
      count += 1
  
  if (x >= len('XMAS')-1 and y <= len(wordsearch[x])-len('XMAS')):
    if (wordsearch[x-1][y+1] == 'M' and wordsearch[x-2][y+2] == 'A' and wordsearch[x-3][y+3] == 'S'):
      count += 1
  
  if (y <= len(wordsearch[x])-len('XMAS')):
    if (wordsearch[x][y+1] == 'M' and wordsearch[x][y+2] == 'A' and wordsearch[x][y+3] == 'S'):
      count += 1
  
  if (x <= len(wordsearch)-len('XMAS') and y <= len(wordsearch[x])-len('XMAS')):
    if (wordsearch[x+1][y+1] == 'M' and wordsearch[x+2][y+2] == 'A' and wordsearch[x+3][y+3] == 'S'):
      count += 1
  
  if (x <= len(wordsearch)-len('XMAS')):
    if (wordsearch[x+1][y] == 'M' and wordsearch[x+2][y] == 'A' and wordsearch[x+3][y] == 'S'):
      count += 1
  
  if (x <= len(wordsearch)-len('XMAS') and y >= len('XMAS')-1):
    if (wordsearch[x+1][y-1] == 'M' and wordsearch[x+2][y-2] == 'A' and wordsearch[x+3][y-3] == 'S'):
      count += 1
  
  if (y >= len('XMAS')-1):
    if (wordsearch[x][y-1] == 'M' and wordsearch[x][y-2] == 'A' and wordsearch[x][y-3] == 'S'):
      count += 1

  return count

def countX_mas(x, y, wordsearch):
  if (wordsearch[x][y] != 'A'):
    return 0
  
  count = 0
  if (x >= 1 and y >= 1 and x <= len(wordsearch)-2 and y <= len(wordsearch[x])-2):
    pair1 = (wordsearch[x-1][y-1], wordsearch[x+1][y+1])
    pair2 = (wordsearch[x+1][y-1], wordsearch[x-1][y+1])
    if ((pair1 == ('M','S') or pair1 == ('S','M')) and (pair2 == ('M','S') or pair2 == ('S','M'))):
      count += 1

  return count

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")
  wordsearch = []

  for line in inputFile:
    wordsearch.append(list(line.strip()))

  inputFile.close()

  xmasOccurrences = 0
  for x in range(len(wordsearch)):
    for y in range(len(wordsearch[0])):
      xmasOccurrences += countXmas(x, y, wordsearch)

  print(xmasOccurrences)


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")
  wordsearch = []

  for line in inputFile:
    wordsearch.append(list(line.strip()))

  inputFile.close()

  x_masOccurrences = 0
  for x in range(len(wordsearch)):
    for y in range(len(wordsearch[0])):
      x_masOccurrences += countX_mas(x, y, wordsearch)

  print(x_masOccurrences)


# Run the code for the specified part ----------------------------------
# partOne("day04/test.txt")
# partOne("day04/input.txt")

# partTwo("day04/test.txt")
partTwo("day04/input.txt")
