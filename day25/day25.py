# Advent of Code 2025 - day25
import pyperclip
from re import findall

def canFit(key, lock):
  for i in range(len(key)):
    if key[i] + lock[i] > 5:
      return False
  return True

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  with open(inputFilePath, "r") as file:
    file_content = file.read()

  puzzleTextRegex = "([#\\.]{5})\\n([#\\.]{5})\\n([#\\.]{5})\\n([#\\.]{5})\\n([#\\.]{5})\\n([#\\.]{5})\\n([#\\.]{5})"
  matches = findall(puzzleTextRegex, file_content)

  locks = []
  keys = []

  for m in matches:
    if m[0] == '#####':
      lock = [-1,-1,-1,-1,-1]
      for h in range(7):
        col = 0
        for char in m[h]:
          if char == '.' and lock[col] == -1:
            lock[col] = h - 1
          col += 1


      locks.append(lock)

    if m[6] == '#####':
      key = [-1,-1,-1,-1,-1]
      for h in range(6,-1,-1):
        col = 0
        for char in m[h]:
          if char == '.' and key[col] == -1:
            key[col] = 5-h
          col += 1

      keys.append(key)

  result = 0

  for k in keys:
    for l in locks:
      if canFit(k, l):
        result += 1

  return result

# Run the code for the specified part ----------------------------------
# answer = partOne("day25/test.txt")
answer = partOne("day25/input.txt")

pyperclip.copy(answer)
print(answer)
