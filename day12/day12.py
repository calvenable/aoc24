# Advent of Code 2025 - day12
import pyperclip
import itertools
from collections import defaultdict

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

steps = [Point(1,0), Point(-1,0), Point(0,1), Point(0,-1)]

def connectedPoints(start:Point, points:list[Point]):
  connected = [start]
  exploring = [start]
  while (exploring):
    node = exploring.pop(0)
    for step in steps:
      potentialStep = node + step
      if potentialStep in points and potentialStep not in connected:
        connected.append(potentialStep)
        exploring.append(potentialStep)

  return connected

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  regions = defaultdict(list[Point])
  x = 0
  for line in inputFile:
    y = 0
    for region in list(line.strip()):
      regions[region].append(Point(x, y))
      y += 1
    x += 1

  inputFile.close()
  
  for r in regions:
    id = 0
    pointParts = dict()
    for point in regions[r]:
      if (point.part == -1):
        if (point in pointParts):
          point.part = pointParts[point]
        else:
          point.part = id
          for p in connectedPoints(point, regions[r]):
            pointParts[p] = id
          id += 1

  result = 0
  for regionName in regions:
    regions[regionName].sort(key=lambda x: x.part)
    parts = [list(g) for _,g in itertools.groupby(regions[regionName], lambda p: p.part)]

    for group in parts:
      partArea = len(group)
      partPerimeter = 0
      for tile in group:
        tilePerimeter = 4
        for step in steps:
          if tile + step in group:
            tilePerimeter -= 1
        partPerimeter += tilePerimeter
      
      # print(regionName)
      # print(str(partArea) + ' * ' + str(partPerimeter) + ' = ' + str(partArea*partPerimeter))
      result += partArea * partPerimeter

  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")

  regions = defaultdict(list[Point])
  x = 0
  for line in inputFile:
    y = 0
    for region in list(line.strip()):
      regions[region].append(Point(x, y))
      y += 1
    x += 1

  inputFile.close()
  
  for r in regions:
    id = 0
    pointParts = dict()
    for point in regions[r]:
      if (point.part == -1):
        if (point in pointParts):
          point.part = pointParts[point]
        else:
          point.part = id
          for p in connectedPoints(point, regions[r]):
            pointParts[p] = id
          id += 1

  result = 0
  for regionName in regions:
    regions[regionName].sort(key=lambda x: x.part)
    parts = [list(g) for _,g in itertools.groupby(regions[regionName], lambda p: p.part)]

    for group in parts:
      partArea = len(group)
      XFences:list[Point] = []
      YFences:list[Point] = []
      for tile in group:
        if (tile + Point(1, 0) not in group):
          XFences.append(Point(tile.x + 0.1, tile.y))
        if (tile + Point(-1, 0) not in group):
          XFences.append(Point(tile.x - 0.1, tile.y))
        if (tile + Point(0, 1) not in group):
          YFences.append(Point(tile.x, tile.y + 0.1))
        if (tile + Point(0, -1) not in group):
          YFences.append(Point(tile.x, tile.y - 0.1))

      XFences.sort(key=lambda p: p.x)
      rows = [list(g) for _,g in itertools.groupby(XFences, lambda p: p.x)]
      XSides = 0
      for row in rows:
        row.sort(key=lambda q: q.y)
        for i in range(len(row)):
          if (i+1 == len(row)):
            XSides += 1
          elif (row[i+1].y - row[i].y > 1):
            XSides += 1

      YFences.sort(key=lambda p: p.y)
      columns = [list(g) for _,g in itertools.groupby(YFences, lambda p: p.y)]
      YSides = 0
      for column in columns:
        column.sort(key=lambda q: q.x)
        for i in range(len(column)):
          if (i+1 == len(column)):
            YSides += 1
          elif (column[i+1].x - column[i].x > 1):
            YSides += 1
        
      # print(regionName)
      # print(str(partArea) + ' * (' + str(XSides) + ' + ' + str(YSides) + ') = ' + str(partArea * (XSides + YSides)))
      result += partArea * (XSides + YSides)

  return result


# Run the code for the specified part ----------------------------------
# answer = partOne("day12/test.txt")
# answer = partOne("day12/input.txt")

# answer = partTwo("day12/test.txt")
answer = partTwo("day12/input.txt")

pyperclip.copy(answer)
print(answer)
