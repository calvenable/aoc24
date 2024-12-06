# Advent of Code 2025 - day06
from enum import IntEnum

class Direction(IntEnum):
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3

def usefulFunction():
  return True


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  map = []
  
  guardpos = [0,0,Direction.UP]
  x = 0
  for line in inputFile:
    if '^' in line:
      # x increases downward, y increases rightward from top-left.
      # Direction.UP is positive x so down the map
      guardpos = [x, line.index('^'), Direction.DOWN]
    map.append(list(line.strip().replace('^','X')))
    x += 1
    
  inputFile.close()
  discovered = 1

  while True:
    if (map[guardpos[0]][guardpos[1]] == '.'):
      map[guardpos[0]][guardpos[1]] = 'X'
      discovered += 1

    lookingAt = ''
    match guardpos[2]:
      case Direction.UP:
        lookingAt = None if guardpos[0] == len(map)-1 else map[guardpos[0]+1][guardpos[1]]
        if lookingAt in ['.','X']:
          guardpos[0] += 1
      case Direction.DOWN:
        lookingAt = None if guardpos[0] == 0 else map[guardpos[0]-1][guardpos[1]]
        if lookingAt in ['.','X']:
          guardpos[0] -= 1
      case Direction.LEFT:
        lookingAt = None if guardpos[1] == len(map[guardpos[0]])-1 else map[guardpos[0]][guardpos[1]+1]
        if lookingAt in ['.','X']:
          guardpos[1] += 1
      case Direction.RIGHT:
        lookingAt = None if guardpos[1] == 0 else map[guardpos[0]][guardpos[1]-1]
        if lookingAt in ['.','X']:
          guardpos[1] -= 1

    if (lookingAt == '#'):
      newDirection = (guardpos[2]+1) % len(Direction)
      guardpos[2] = Direction(newDirection)

    if (lookingAt == None):
      break

  print(discovered)


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  return False


# Run the code for the specified part ----------------------------------
# partOne("day06/test.txt")
partOne("day06/input.txt")

# partTwo("day06/test.txt")
# partTwo("day06/input.txt")
