# Advent of Code 2025 - day16
import pyperclip
from enum import IntEnum

class Direction(IntEnum):
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3

class Reindeer():
  def __init__(self, x, y, direction, previous = [], hasTurned = False, score=0):
    self.x = x
    self.y = y
    self.dir = direction
    self.prev = previous
    self.hasTurned = hasTurned
    self.score = score

  def __eq__(self, other):
    return (self.x, self.y, self.dir) == (other.x, other.y, other.dir)

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  map = []
  reindeers:list[Reindeer] = []

  x=0
  with open(inputFilePath, "r") as file:
    for line in file:
      map.append(list(line.strip()))
      if 'S' in line:
        reindeers.append(Reindeer(x, line.index('S'), Direction.RIGHT))
      x += 1

  lowest = 100000000000
  lowestToLoc:list[Reindeer] = []
  count = 0
  while (reindeers):
    reindeer = reindeers.pop(0)

    # Keep a list of the lowest score to get to every location
    try:
      ind = lowestToLoc.index(reindeer)
      lowestSoFar = lowestToLoc[ind]
      if reindeer.score < lowestSoFar.score:
        lowestToLoc[ind] = reindeer
      else:
        continue
    except ValueError:
      lowestToLoc.append(reindeer)

    if map[reindeer.x][reindeer.y] == 'E':
      if reindeer.score < lowest:
        lowest = reindeer.score
      continue

    # Try: move forward, turn left (if not turned before), turn right (if not turned on this space before)
    match reindeer.dir:
      case Direction.UP:
        if map[reindeer.x-1][reindeer.y] != '#' and (reindeer.x - 1, reindeer.y) not in reindeer.prev:
          reindeers.append(Reindeer(reindeer.x - 1, reindeer.y, reindeer.dir, reindeer.prev + [(reindeer.x, reindeer.y)], False, reindeer.score + 1))
        if not reindeer.hasTurned:
          if map[reindeer.x][reindeer.y+1] != '#':
            reindeers.append(Reindeer(reindeer.x, reindeer.y, (reindeer.dir + 1) % len(Direction), reindeer.prev, True, reindeer.score + 1000))
          if map[reindeer.x][reindeer.y-1] != '#':
            reindeers.append(Reindeer(reindeer.x, reindeer.y, (reindeer.dir + 3) % len(Direction), reindeer.prev, True, reindeer.score + 1000))
      
      case Direction.DOWN:
        if map[reindeer.x+1][reindeer.y] != '#' and (reindeer.x + 1, reindeer.y) not in reindeer.prev:
          reindeers.append(Reindeer(reindeer.x + 1, reindeer.y, reindeer.dir, reindeer.prev + [(reindeer.x, reindeer.y)], False, reindeer.score + 1))
        if not reindeer.hasTurned:
          if map[reindeer.x][reindeer.y+1] != '#':
            reindeers.append(Reindeer(reindeer.x, reindeer.y, (reindeer.dir + 3) % len(Direction), reindeer.prev, True, reindeer.score + 1000))
          if map[reindeer.x][reindeer.y-1] != '#':
            reindeers.append(Reindeer(reindeer.x, reindeer.y, (reindeer.dir + 1) % len(Direction), reindeer.prev, True, reindeer.score + 1000))
      
      case Direction.LEFT:
        if map[reindeer.x][reindeer.y-1] != '#' and (reindeer.x, reindeer.y - 1) not in reindeer.prev:
          reindeers.append(Reindeer(reindeer.x, reindeer.y - 1, reindeer.dir, reindeer.prev + [(reindeer.x, reindeer.y)], False, reindeer.score + 1))
        if not reindeer.hasTurned:
          if map[reindeer.x-1][reindeer.y] != '#':
            reindeers.append(Reindeer(reindeer.x, reindeer.y, (reindeer.dir + 1) % len(Direction), reindeer.prev, True, reindeer.score + 1000))
          if map[reindeer.x+1][reindeer.y] != '#':
            reindeers.append(Reindeer(reindeer.x, reindeer.y, (reindeer.dir + 3) % len(Direction), reindeer.prev, True, reindeer.score + 1000))
      
      case Direction.RIGHT:
        if map[reindeer.x][reindeer.y+1] != '#' and (reindeer.x, reindeer.y + 1) not in reindeer.prev:
          reindeers.append(Reindeer(reindeer.x, reindeer.y + 1, reindeer.dir, reindeer.prev + [(reindeer.x, reindeer.y)], False, reindeer.score + 1))
        if not reindeer.hasTurned:
          if map[reindeer.x+1][reindeer.y] != '#':
            reindeers.append(Reindeer(reindeer.x, reindeer.y, (reindeer.dir + 1) % len(Direction), reindeer.prev, True, reindeer.score + 1000))
          if map[reindeer.x-1][reindeer.y] != '#':
            reindeers.append(Reindeer(reindeer.x, reindeer.y, (reindeer.dir + 3) % len(Direction), reindeer.prev, True, reindeer.score + 1000))

    count += 1
    if count % 1000000 == 0:
      print("lowest: " + str(lowest) + " at iteration " + str(count/1000000) + " million, reindeer left = " + str(len(reindeers)))
  return lowest


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  return False


# Run the code for the specified part ----------------------------------
# answer = partOne("day16/test.txt")
answer = partOne("day16/input.txt")

# answer = partTwo("day16/test.txt")
# answer = partTwo("day16/input.txt")

pyperclip.copy(answer)
print(answer)
