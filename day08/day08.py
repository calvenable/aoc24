# Advent of Code 2025 - day08
from regex import match

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

def isAntenna(p:Point, antennae:dict[str, list[Point]]):
  antennaList = []
  for l in antennae.values():
    antennaList += l
  return p in antennaList

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  antennae = dict()
  y = 0
  x = 0
  for line in inputFile:
    x = 0
    for antenna in line:
      if match("[0-9a-zA-Z]", antenna):
        if antenna in antennae:
          antennae[antenna].append(Point(x, y))
        else:
          antennae[antenna] = [Point(x, y)]
      x += 1
    y += 1

  inputFile.close()

  maxWidth = x - 1
  maxHeight = y - 1
  antinodes = []

  for type in antennae:
    pairs = [(a, b) for idx, a in enumerate(antennae[type]) for b in antennae[type][idx + 1:]]
    for pair in pairs:
      vectorBetween = pair[1] - pair[0]
      antinode1:Point = pair[1] + vectorBetween
      antinode2:Point = pair[0] - vectorBetween

      if antinode1.inBounds(0,0,maxWidth,maxHeight):# and not isAntenna(antinode1, antennae):
        antinodes.append(antinode1)
      if antinode2.inBounds(0,0,maxWidth,maxHeight):# and not isAntenna(antinode2, antennae):
        antinodes.append(antinode2)

  antinodes = list(set(antinodes))

  return len(antinodes)


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")

  antennae = dict()
  y = 0
  x = 0
  for line in inputFile:
    x = 0
    for antenna in line:
      if match("[0-9a-zA-Z]", antenna):
        if antenna in antennae:
          antennae[antenna].append(Point(x, y))
        else:
          antennae[antenna] = [Point(x, y)]
      x += 1
    y += 1

  inputFile.close()

  maxWidth = x - 1
  maxHeight = y - 1
  antinodes = []

  for type in antennae:
    pairs = [(a, b) for idx, a in enumerate(antennae[type]) for b in antennae[type][idx + 1:]]
    for pair in pairs:
      vectorBetween = pair[1] - pair[0]

      potentialAntinodes = [pair[0], pair[1]]
      for i in range(1,maxWidth):
        potentialAntinodes.append(pair[1] + (vectorBetween * i))
      for i in range(1,maxWidth):
        potentialAntinodes.append(pair[0] - (vectorBetween * i))

      for a in potentialAntinodes:
        if a.inBounds(0,0,maxWidth,maxHeight):
          antinodes.append(a)

  antinodes = list(set(antinodes))

  return len(antinodes)


# Run the code for the specified part ----------------------------------
# print(partOne("day08/test.txt"))
# print(partOne("day08/input.txt"))

# print(partTwo("day08/test.txt"))
print(partTwo("day08/input.txt"))
