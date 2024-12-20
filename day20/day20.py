# Advent of Code 2025 - day20
import pyperclip

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
  
  def distanceTo(self, other):
    if isinstance(other, Point):
      return abs(other.x - self.x) + abs(other.y - self.y)
    return NotImplemented
  
  def inBounds(self, minX, minY, maxX, maxY):
    '''Return true if the point is within or on the boundary values provided'''
    return self.x >= minX and self.x <= maxX and self.y >= minY and self.y <= maxY

directions = [Point(0,1), Point(1,0), Point(0,-1), Point(-1,0)]

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  track = []
  start = Point(0,0)
  end = Point(0,0)

  y=0
  with open(inputFilePath, "r") as file:
    for line in file:
      track.append(list(line.strip()))
      if 'S' in line:
        start = Point(line.index('S'), y)
      if 'E' in line:
        end = Point(line.index('E'), y)
      y += 1

  # Follow the path to find the shortest time pre-cheat
  racePath = [start]
  while (racePath[-1] != end):
    for d in directions:
      step = racePath[-1] + d
      if (track[step.y][step.x] != '#' and (len(racePath) == 1 or step != racePath[-2])):
        racePath.append(step)
        break

  save100orMoreCheats = 0

  for tile in racePath:
    for d1 in [d1 for d1 in directions if track[(tile+d1).y][(tile+d1).x] == '#']:
      # No going back on yourself, going out of bounds, or ending on a wall
      for d2 in [d for d in directions if d+d1!=Point(0,0) and (tile+d1+d).inBounds(0,0,len(track[0])-1,len(track)-1) and track[(tile+d1+d).y][(tile+d1+d).x] != '#']:
        timeSaved = racePath.index(tile+d1+d2) - racePath.index(tile) - 2
        if timeSaved >= 100:
          save100orMoreCheats += 1

  return save100orMoreCheats


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  track = []
  start = Point(0,0)
  end = Point(0,0)

  y=0
  with open(inputFilePath, "r") as file:
    for line in file:
      track.append(list(line.strip()))
      if 'S' in line:
        start = Point(line.index('S'), y)
      if 'E' in line:
        end = Point(line.index('E'), y)
      y += 1

  # Follow the path to find the shortest time pre-cheat
  racePath = [start]
  while (racePath[-1] != end):
    for d in directions:
      step = racePath[-1] + d
      if (track[step.y][step.x] != '#' and (len(racePath) == 1 or step != racePath[-2])):
        racePath.append(step)
        break

  save100orMoreCheats = 0

  for index in range(len(racePath)):
    for futureTileIndex in range(index + 1, len(racePath)):
      distance = racePath[index].distanceTo(racePath[futureTileIndex])
      if distance > 1 and distance <= 20:

        timeSaved = futureTileIndex - index - distance
        if timeSaved >= 100:
          save100orMoreCheats += 1
    
  return save100orMoreCheats


# Run the code for the specified part ----------------------------------
# answer = partOne("day20/test.txt")
# answer = partOne("day20/input.txt")

# answer = partTwo("day20/test.txt")
answer = partTwo("day20/input.txt")

pyperclip.copy(answer)
print(answer)
