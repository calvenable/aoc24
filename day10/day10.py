# Advent of Code 2025 - day10
from enum import IntEnum
import pyperclip

class Direction(IntEnum):
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3

class Point():
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")"

  def __eq__(self, other):
    if (isinstance(other, Point)):
      return (self.x, self.y) == (other.x, other.y)
    return NotImplemented
  
  def __hash__(self):
    return hash((self.x, self.y))
  
  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)
  
  def __add__(self, other):
    return Point(other.x + self.x, other.y + self.y)
  
  def __mul__(self, other):
    return Point(self.x * other, self.y * other)
  
  def inBounds(self, minX, minY, maxX, maxY):
    '''Return true if the point is within or on the boundary values provided'''
    return self.x >= minX and self.x <= maxX and self.y >= minY and self.y <= maxY
  
steps = [Point(1,0), Point(-1,0), Point(0,1), Point(0,-1)]

class Hiker():
  def __init__(self, x, y, height, trailhead=None, prevx=None, prevy=None):
    self.loc = Point(x, y)
    self.height = height
    if (trailhead is not None):
      self.trailhead = trailhead
    else:
      self.trailhead = self.loc
    if (prevx is not None and prevy is not None):
      self.prevLoc = Point(prevx, prevy)
    else:
      self.prevLoc = None


  

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  heightMap:list[int] = []
  trailheads:list[Point] = []
  x = 0
  for line in inputFile:
    heightMap.append(list(map(int, list(line.strip()))))
    for i in range(len(heightMap[-1])):
      if heightMap[-1][i] == 0:
        trailheads.append(Point(x, i))
    x += 1

  inputFile.close()
  maxHeight = len(heightMap)
  maxWidth = len(heightMap[0])

  hikers:list[Hiker] = []
  for t in trailheads:
    hikers.append(Hiker(t.x, t.y, 0))

  peaks:dict[Point, list[Point]] = dict()
  while (hikers):
    frontHiker = hikers.pop(0)

    if (frontHiker.height == 9):
      if (frontHiker.trailhead in peaks):
        peaks[frontHiker.trailhead].append(frontHiker.loc)
      else:
        peaks[frontHiker.trailhead] = [frontHiker.loc]
      continue

    for step in steps:
      nextStep:Point = frontHiker.loc + step
      if (nextStep != frontHiker.prevLoc and nextStep.inBounds(0,0,maxHeight-1,maxWidth-1)):
        nextHeight = heightMap[nextStep.x][nextStep.y]
        if (nextHeight == frontHiker.height + 1):
          hikers.append(Hiker(nextStep.x, nextStep.y, nextHeight, frontHiker.trailhead, frontHiker.loc.x, frontHiker.loc.y))


  return sum([len(list(set(theadPeaks))) for theadPeaks in peaks.values()])


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")

  heightMap:list[int] = []
  trailheads:list[Point] = []
  x = 0
  for line in inputFile:
    heightMap.append(list(map(int, list(line.strip()))))
    for i in range(len(heightMap[-1])):
      if heightMap[-1][i] == 0:
        trailheads.append(Point(x, i))
    x += 1

  inputFile.close()
  maxHeight = len(heightMap)
  maxWidth = len(heightMap[0])

  hikers:list[Hiker] = []
  for t in trailheads:
    hikers.append(Hiker(t.x, t.y, 0))

  peaks:dict[Point, list[Point]] = dict()
  while (hikers):
    frontHiker = hikers.pop(0)

    if (frontHiker.height == 9):
      if (frontHiker.trailhead in peaks):
        peaks[frontHiker.trailhead].append(frontHiker.loc)
      else:
        peaks[frontHiker.trailhead] = [frontHiker.loc]
      continue

    for step in steps:
      nextStep:Point = frontHiker.loc + step
      if (nextStep != frontHiker.prevLoc and nextStep.inBounds(0,0,maxHeight-1,maxWidth-1)):
        nextHeight = heightMap[nextStep.x][nextStep.y]
        if (nextHeight == frontHiker.height + 1):
          hikers.append(Hiker(nextStep.x, nextStep.y, nextHeight, frontHiker.trailhead, frontHiker.loc.x, frontHiker.loc.y))


  return sum([len(theadPeaks) for theadPeaks in peaks.values()])


# Run the code for the specified part ----------------------------------
# answer = partOne("day10/test.txt")
# answer = partOne("day10/input.txt")

answer = partTwo("day10/test.txt")
# answer = partTwo("day10/input.txt")

pyperclip.copy(answer)
print(answer)
