# Advent of Code 2025 - day15
import pyperclip

class Point():
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


def canMove(grid:list[list[str]], start:Point, direction:Point):
  moveTo:Point = start + direction
  match grid[moveTo.x][moveTo.y]:
    case '.':
      return True
    case 'O':
      return canMove(grid, moveTo, direction)
    case '#':
      return False
    case _:
      return False

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  warehouse:list[list[str]] = []
  instructions:list[str] = []
  readingInstructions = False
  robot = Point(0,0)

  y = 0
  with open(inputFilePath, "r") as file:
    for line in file:
      if (readingInstructions):
        instructions += list(line.strip())
      else:
        if len(line) > 2:
          if len(warehouse) == 0:
            for i in range(len(line)):
              warehouse.append([line[i]])
          else:
            for i in range(len(line)):
              warehouse[i].append(line[i])
            
          if '@' in line:
            robot = Point(line.index('@'), y)

        else:
          readingInstructions = True

      y += 1

  directions:dict[str, Point] = dict()
  directions['<'] = Point(-1,0)
  directions['^'] = Point(0,-1)
  directions['>'] = Point(1,0)
  directions['v'] = Point(0,1)

  for instruction in instructions:
    direction = directions[instruction]
    if canMove(warehouse, robot, direction):
      currentSpace = robot
      newSpace = currentSpace + direction
      warehouse[currentSpace.x][currentSpace.y] = '.'
      tempOut = warehouse[newSpace.x][newSpace.y]
      warehouse[newSpace.x][newSpace.y] = '@'
      robot += direction

      while tempOut != '.':
        newSpace += direction
        tempIn = warehouse[newSpace.x][newSpace.y]
        warehouse[newSpace.x][newSpace.y] = tempOut
        tempOut = tempIn


  result = 0
  for x in range(len(warehouse)):
    for y in range(len(warehouse[x])):
      if warehouse[x][y] == 'O':
        result += x + (100 * y)
        
  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  warehouse:list[list[str]] = []
  instructions:list[str] = []
  readingInstructions = False
  robot = Point(0,0)

  y = 0
  with open(inputFilePath, "r") as file:
    for line in file:
      if (readingInstructions):
        instructions += list(line.strip())
      else:
        if len(line) > 2:
          if len(warehouse) == 0:
            for i in range(len(line)):
              warehouse.append(['#','#'])
          else:
            for i in range(len(line)):
              match line[i]:
                case '#':
                  warehouse[i] += ['#', '#']
                case '.':
                  warehouse[i] += ['.', '.']
                case 'O':
                  warehouse[i] += ['[', ']']
                case '@':
                  warehouse[i] += ['@', '.']
            
          if '@' in line:
            robot = Point(2*line.index('@'), y)

        else:
          readingInstructions = True

      y += 1

  directions:dict[str, Point] = dict()
  directions['<'] = Point(-1,0)
  directions['^'] = Point(0,-1)
  directions['>'] = Point(1,0)
  directions['v'] = Point(0,1)

  for instruction in instructions:
    direction = directions[instruction]
    # TODO: Update canMove to check the current column
    # and columns of adjacent box pieces if pushing up or down
    if canMove(warehouse, robot, direction):
      # TODO: Update stepping and char moving to include adjacent columns
      # if pushing vertically and tempOut = '[' or ']'
      currentSpace = robot
      newSpace = currentSpace + direction
      warehouse[currentSpace.x][currentSpace.y] = '.'
      tempOut = warehouse[newSpace.x][newSpace.y]
      warehouse[newSpace.x][newSpace.y] = '@'
      robot += direction

      while tempOut != '.':
        newSpace += direction
        tempIn = warehouse[newSpace.x][newSpace.y]
        warehouse[newSpace.x][newSpace.y] = tempOut
        tempOut = tempIn


  result = 0
  for x in range(len(warehouse)):
    for y in range(len(warehouse[x])):
      if warehouse[x][y] == 'O':
        result += x + (100 * y)
        
  return result


# Run the code for the specified part ----------------------------------
# answer = partOne("day15/test.txt")
answer = partOne("day15/input.txt")

# answer = partTwo("day15/test.txt")
# answer = partTwo("day15/input.txt")

pyperclip.copy(answer)
print(answer)
