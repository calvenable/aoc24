# Advent of Code 2025 - day06
from enum import IntEnum

class Direction(IntEnum):
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3

class Guard:
  def __init__(self, x=0, y=0, direction=Direction.DOWN):
    self.x = x
    self.y = y
    self.direction = direction

  def turn(self):
    '''Turn the guard right 90 degrees'''
    self.direction = (self.direction + 1) % len(Direction)

  def __eq__(self, other):
    if isinstance(other, Guard):
      return (self.x, self.y, self.direction) == (other.x, other.y, other.direction)
    return NotImplemented


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  map = []
  
  x = 0
  for line in inputFile:
    if '^' in line:
      # x increases downward, y increases rightward from top-left.
      # Direction.UP is positive x so down the map
      guard = Guard(x, line.index('^'), Direction.DOWN)

    map.append(list(line.strip().replace('^','X')))
    x += 1
    
  inputFile.close()
  discovered = 1

  while True:
    if (map[guard.x][guard.y] == '.'):
      map[guard.x][guard.y] = 'X'
      discovered += 1

    lookingAt = ''
    match guard.direction:
      case Direction.UP:
        lookingAt = None if guard.x == len(map)-1 else map[guard.x+1][guard.y]
        if lookingAt in ['.','X']:
          guard.x += 1
      case Direction.DOWN:
        lookingAt = None if guard.x == 0 else map[guard.x-1][guard.y]
        if lookingAt in ['.','X']:
          guard.x -= 1
      case Direction.LEFT:
        lookingAt = None if guard.y == len(map[guard.x])-1 else map[guard.x][guard.y+1]
        if lookingAt in ['.','X']:
          guard.y += 1
      case Direction.RIGHT:
        lookingAt = None if guard.y == 0 else map[guard.x][guard.y-1]
        if lookingAt in ['.','X']:
          guard.y -= 1

    if (lookingAt == '#'):
      guard.turn()

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
