# Advent of Code 2025 - day11
import pyperclip

def iterateStones(stones):
  newStones:dict[int, int] = dict()

  for x in stones.keys():
    if (x == 0):
      if (1 in newStones):
        newStones[1] += stones[x]
      else:
        newStones[1] = stones[x]

    elif (len(str(x)) % 2 == 0):
      firstStone = int(str(x)[:len(str(x)) // 2])
      secondStone = int(str(x)[len(str(x)) // 2:])
      if (firstStone in newStones):
        newStones[firstStone] += stones[x]
      else:
        newStones[firstStone] = stones[x]
      if (secondStone in newStones):
        newStones[secondStone] += stones[x]
      else:
        newStones[secondStone] = stones[x]

    else:
      newStones[x*2024] = stones[x]

  return newStones

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  stones:dict[int, int] = dict()
  for line in inputFile:
    for stone in list(map(int, line.strip().split(' '))):
      if (stone in stones):
        stones[stone] += 1
      else:
        stones[stone] = 1

  inputFile.close()
  
  blinks = 25
  for _ in range(blinks):
    stones = iterateStones(stones)
    # print(stones)

  return sum(stones.values())


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")

  stones:dict[int, int] = dict()
  for line in inputFile:
    for stone in list(map(int, line.strip().split(' '))):
      if (stone in stones):
        stones[stone] += 1
      else:
        stones[stone] = 1

  inputFile.close()
  
  blinks = 75
  for _ in range(blinks):
    stones = iterateStones(stones)
    # print(stones)

  return sum(stones.values())


# Run the code for the specified part ----------------------------------
# answer = partOne("day11/test.txt")
# answer = partOne("day11/input.txt")

# answer = partTwo("day11/test.txt")
answer = partTwo("day11/input.txt")

pyperclip.copy(answer)
print(answer)
