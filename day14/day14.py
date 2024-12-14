# Advent of Code 2025 - day14
import pyperclip
from re import findall

def usefulFunction():
  return True

class Point():
  part = -1
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")"

  def __repr__(self):
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

class Robot():
  def __init__(self, location:Point, velocity:Point):
    self.location = location
    self.velocity = velocity

  def move(self, upperXbound, upperYbound):
    """Move the robot one step according to its current velocity"""
    self.location += self.velocity

    if self.location.x >= upperXbound:
      self.location.x -= upperXbound
    if self.location.x < 0:
      self.location.x += upperXbound

    if self.location.y >= upperYbound:
      self.location.y -= upperYbound
    if self.location.y < 0:
      self.location.y += upperYbound

  def isAdjacent(self, other):
    return abs(self.location.x - other.location.x) <= 1 and abs(self.location.y - other.location.y) <= 1


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  with open(inputFilePath, "r") as file:
    file_content = file.read()

  puzzleTextRegex = "p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)\\n"
  matches = findall(puzzleTextRegex, file_content)

  robots:list[Robot] = []
  for match in matches:
    (Px, Py, Vx, Vy) = list(map(int, match))
    robots.append(Robot(Point(Px, Py), Point(Vx, Vy)))

  
  result = 0
  width = 101
  height = 103

  simulationSeconds = 100000
  for _ in range(simulationSeconds):
    for r in robots:
      r.move(width, height)

  (tl, tr, bl, br) = (0,0,0,0)
  dividingX = (width-1)/2
  dividingY = (height-1)/2
  for r in robots:
    if r.location.x < dividingX and r.location.y < dividingY:
      tl += 1
    elif r.location.x > dividingX and r.location.y < dividingY:
      tr += 1
    elif r.location.x < dividingX and r.location.y > dividingY:
      bl += 1
    elif r.location.x > dividingX and r.location.y > dividingY:
      br += 1
  
  return tl * tr * bl * br


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  with open(inputFilePath, "r") as file:
    file_content = file.read()

  puzzleTextRegex = "p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)\\n"
  matches = findall(puzzleTextRegex, file_content)

  robots:list[Robot] = []
  for match in matches:
    (Px, Py, Vx, Vy) = list(map(int, match))
    robots.append(Robot(Point(Px, Py), Point(Vx, Vy)))

  width = 101
  height = 103

  simulationSeconds = 10000
  for s in range(simulationSeconds):
    for r in robots:
      r.move(width, height)

    robotMap:list[list[int]] = list()
    for x in range(width):
      robotMap.append([])
      for y in range(height):
        robotMap[x].append([])
        robotMap[x][y] = '.'

    for robot in robots:
      robotMap[robot.location.x][robot.location.y] = '#'

    adjacentCount = 0
    for r1 in range(len(robots)):
      for r2 in range(r1, len(robots)):
        if robots[r1].isAdjacent(robots[r2]):
          adjacentCount += 1

    if adjacentCount > 1200:
      for y in range(len(robotMap[0])):
        for x in range(len(robotMap)):
          print(robotMap[x][y], end='')
        print()
      print(adjacentCount)

      print(str(s+1))

      input()


# Run the code for the specified part ----------------------------------
# answer = partOne("day14/test.txt")
# answer = partOne("day14/input.txt")

# answer = partTwo("day14/test.txt")
answer = partTwo("day14/input.txt")

pyperclip.copy(answer)
print(answer)
