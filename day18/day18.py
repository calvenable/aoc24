# Advent of Code 2025 - day18
import pyperclip

class Explorer():
  def __init__(self, x, y, steps, previous = []):
    self.x = x
    self.y = y
    self.steps = steps
    self.prev = previous

  def __eq__(self, other):
    if isinstance(other, Explorer):
      return (self.x, self.y) == (other.x, other.y)
    return NotImplemented
  
  def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")[" + str(self.steps) + "]"
  
  def __repr__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")[" + str(self.steps) + "]"

def inSquare(pos:tuple, min, max):
  return pos[0] >= min and pos[1] >= min and pos[0] <= max and pos[1] <= max

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath, minCoord, maxCoord, bytesToProcess):

  memoryGrid:list[list[bool]] = []
  for _ in range(maxCoord - minCoord):
    memoryGrid.append([])
    for _ in range(maxCoord - minCoord):
      memoryGrid[-1].append(False)

  count = 0
  with open(inputFilePath, "r") as file:
    for line in file:
      if count == bytesToProcess:
        break
      coords = list(map(int, line.strip().split(',')))
      memoryGrid[coords[0]][coords[1]] = True
      count += 1

  explorers = [Explorer(0,0,0)]
  lowestToLoc:list[Explorer] = []

  count = 0
  while (explorers):
    explorer = explorers.pop(0)

    try:
      ind = lowestToLoc.index(explorer)
      lowestSoFar = lowestToLoc[ind]
      if explorer.steps < lowestSoFar.steps:
        lowestToLoc[ind] = explorer
      else:
        continue
    except ValueError:
      lowestToLoc.append(explorer)

    if (explorer.x, explorer.y) == (maxCoord-1, maxCoord-1):
      continue

    if inSquare((explorer.x, explorer.y + 1), minCoord, maxCoord-1) and not memoryGrid[explorer.x][explorer.y + 1] and (explorer.x, explorer.y+1) not in explorer.prev:
      explorers.append(Explorer(explorer.x, explorer.y+1, explorer.steps+1, explorer.prev + [(explorer.x, explorer.y)]))
    
    if inSquare((explorer.x, explorer.y - 1), minCoord, maxCoord-1) and not memoryGrid[explorer.x][explorer.y - 1] and (explorer.x, explorer.y-1) not in explorer.prev:
      explorers.append(Explorer(explorer.x, explorer.y-1, explorer.steps+1, explorer.prev + [(explorer.x, explorer.y)]))
    
    if inSquare((explorer.x + 1, explorer.y), minCoord, maxCoord-1) and not memoryGrid[explorer.x + 1][explorer.y] and (explorer.x+1, explorer.y) not in explorer.prev:
      explorers.append(Explorer(explorer.x + 1, explorer.y, explorer.steps+1, explorer.prev + [(explorer.x, explorer.y)]))
    
    if inSquare((explorer.x - 1, explorer.y), minCoord, maxCoord-1) and not memoryGrid[explorer.x - 1][explorer.y] and (explorer.x-1, explorer.y) not in explorer.prev:
      explorers.append(Explorer(explorer.x - 1, explorer.y, explorer.steps+1, explorer.prev + [(explorer.x, explorer.y)]))

  try:
    index = lowestToLoc.index(Explorer(maxCoord-1, maxCoord-1, 0))
    return lowestToLoc[index].steps
  except ValueError:
    return -1


def shortestPath(memoryGrid, minCoord, maxCoord):
  explorers = [Explorer(0,0,0)]
  lowestToLoc:list[Explorer] = []

  while (explorers):
    explorer = explorers.pop(0)

    try:
      ind = lowestToLoc.index(explorer)
      lowestSoFar = lowestToLoc[ind]
      if explorer.steps < lowestSoFar.steps:
        lowestToLoc[ind] = explorer
      else:
        continue
    except ValueError:
      lowestToLoc.append(explorer)

    if (explorer.x, explorer.y) == (maxCoord-1, maxCoord-1):
      continue

    if inSquare((explorer.x, explorer.y + 1), minCoord, maxCoord-1) and not memoryGrid[explorer.x][explorer.y + 1] and (explorer.x, explorer.y+1) not in explorer.prev:
      explorers.append(Explorer(explorer.x, explorer.y+1, explorer.steps+1, explorer.prev + [(explorer.x, explorer.y)]))
    
    if inSquare((explorer.x, explorer.y - 1), minCoord, maxCoord-1) and not memoryGrid[explorer.x][explorer.y - 1] and (explorer.x, explorer.y-1) not in explorer.prev:
      explorers.append(Explorer(explorer.x, explorer.y-1, explorer.steps+1, explorer.prev + [(explorer.x, explorer.y)]))
    
    if inSquare((explorer.x + 1, explorer.y), minCoord, maxCoord-1) and not memoryGrid[explorer.x + 1][explorer.y] and (explorer.x+1, explorer.y) not in explorer.prev:
      explorers.append(Explorer(explorer.x + 1, explorer.y, explorer.steps+1, explorer.prev + [(explorer.x, explorer.y)]))
    
    if inSquare((explorer.x - 1, explorer.y), minCoord, maxCoord-1) and not memoryGrid[explorer.x - 1][explorer.y] and (explorer.x-1, explorer.y) not in explorer.prev:
      explorers.append(Explorer(explorer.x - 1, explorer.y, explorer.steps+1, explorer.prev + [(explorer.x, explorer.y)]))

  try:
    index = lowestToLoc.index(Explorer(maxCoord-1, maxCoord-1, 0))
    return lowestToLoc[index].prev
  except ValueError:
    return []


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath, minCoord, maxCoord, bytesToStart):

  # Set up an array of arrays the right size
  memoryGrid:list[list[bool]] = []
  for _ in range(maxCoord - minCoord):
    memoryGrid.append([])
    for _ in range(maxCoord - minCoord):
      memoryGrid[-1].append(False)

  count = 0
  previousShortestPath = []
  with open(inputFilePath, "r") as file:
    for line in file:
      # Get the coords and mark the spot as corrupted
      coords = list(map(int, line.strip().split(',')))
      memoryGrid[coords[0]][coords[1]] = True

      # If more bytes have fallen than the safe number found in part 1
      # and the newly corrupted tile is on the previous shortest path
      if count > bytesToStart and ((coords[0], coords[1]) in previousShortestPath or len(previousShortestPath) == 0):
        # Try and find a new shortest path to the exit
        previousShortestPath = shortestPath(memoryGrid, minCoord, maxCoord)
        if len(previousShortestPath) == 0:
          # If there is no new shortest path, we've found the blocker!
          return str(coords[0]) + "," + str(coords[1])
      count += 1
  


# Run the code for the specified part ----------------------------------
# answer = partOne("day18/test.txt", 0, 7, 12)
# answer = partOne("day18/input.txt", 0, 71, 1024)

# answer = partTwo("day18/test.txt", 0, 7, 12)
answer = partTwo("day18/input.txt", 0, 71, 1024)

pyperclip.copy(answer)
print(answer)
