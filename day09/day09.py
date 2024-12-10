# Advent of Code 2025 - day09

import operator

def rindex(lst, value):
    return len(lst) - operator.indexOf(reversed(lst), value) - 1

class DiskItem():
  def __init__(self, spaces:int, id:str=None):
    self.length = spaces
    self.dir:list[str] = []
    for _ in range(spaces):
      self.dir.append(id)

  def __str__(self):
    result = ''
    for item in self.dir:
      if item is None:
        result += '.'
      else:
        result += str(item)
    return result
  
  def toList(self):
    result = []
    for item in self.dir:
      if item is None:
        result.append(0)
      else:
        result.append(int(item))
    return result

  def countEmptySpaces(self):
    return sum(x is None for x in self.dir)

  def countFullSpaces(self):
    return sum(x is not None for x in self.dir)
  
  def hasEmptySpace(self):
    try:
      self.dir.index(None)
      return True
    except ValueError:
      return False
  
  def moveIn(self, id):
    if (self.hasEmptySpace()):
      self.dir[self.dir.index(None)] = id
      return self.hasEmptySpace()
    return False

  def moveOut(self):
    items = [x for x in self.dir if x is not None]
    if (len(items) > 0):
      itemToRemove = items.pop()
      index = rindex(self.dir, itemToRemove)
      self.dir[index] = None
      return itemToRemove
    
    return None

def lastNonEmptyBlock(hardDrive:list[DiskItem]):
  return rindex([di.countFullSpaces() > 0 for di in hardDrive], True)

def firstNonFullBlock(hardDrive:list[DiskItem]):
  return [di.hasEmptySpace() for di in hardDrive].index(True)

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  hardDrive:list[DiskItem] = []

  for line in inputFile:
    isFree = False
    id = 0
    for x in list(map(int, list(line.strip()))):
      if (isFree):
        # TODO: I should not have put these into class objects
        # Using an integer list would have been much faster!
        hardDrive.append(DiskItem(x))
      else:
        hardDrive.append(DiskItem(x, id))
        id += 1
      isFree = not isFree

  inputFile.close()

  lastFullSpaceIndex = lastNonEmptyBlock(hardDrive)
  firstEmptySpaceIndex = firstNonFullBlock(hardDrive)
  while (lastFullSpaceIndex > firstEmptySpaceIndex):
    if (not hardDrive[firstEmptySpaceIndex].moveIn(hardDrive[lastFullSpaceIndex].moveOut())):
      firstEmptySpaceIndex = firstNonFullBlock(hardDrive)
    
    if (hardDrive[-1].countFullSpaces() == 0):
      hardDrive.pop()

    lastFullSpaceIndex = lastNonEmptyBlock(hardDrive)

  blockList = []
  for diskitem in hardDrive:
    blockList += diskitem.toList()
  return sum([i*x for i,x in enumerate(blockList)])


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")

  hardDrive:list[DiskItem] = []

  for line in inputFile:
    isFree = False
    id = 0
    for x in list(map(int, list(line.strip()))):
      if (isFree):
        # TODO: I should not have put these into class objects
        # Using an integer list would have been much faster!
        hardDrive.append(DiskItem(x))
      else:
        hardDrive.append(DiskItem(x, id))
        id += 1
      isFree = not isFree

  inputFile.close()

  for fullFile in [x for x in hardDrive if not x.hasEmptySpace()]:
    # Find the first DiskItem that has enough space for fullFile.length
    # If it is to the left of fullFile:
    # Move the whole file (repeatedly move chars until empty)
    pass

  blockList = []
  for diskitem in hardDrive:
    blockList += diskitem.toList()
  return sum([i*x for i,x in enumerate(blockList)])


# Run the code for the specified part ----------------------------------
# print(partOne("day09/test.txt"))
# print(partOne("day09/input.txt"))

print(partTwo("day09/test.txt"))
# print(partTwo("day09/input.txt"))
