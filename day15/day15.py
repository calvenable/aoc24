# Advent of Code 2025 - day15
import pyperclip

wideWarehouse:list[list[str]] = []

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
    case '[':
      if direction in [Point(0,1), Point(0,-1)]:
        # Check vertically past [ and corresponding ]
        return canMove(grid, moveTo, direction) and canMove(grid, moveTo+Point(1,0), direction)
      else:
        # Continue checking horizontally past the second tile of the box
        return canMove(grid, moveTo + direction, direction)
    case ']':
      if direction in [Point(0,1), Point(0,-1)]:
        # Check vertically past ] and corresponding [
        return canMove(grid, moveTo, direction) and canMove(grid, moveTo+Point(-1,0), direction)
      else:
        # Continue checking horizontally past the second tile of the box
        return canMove(grid, moveTo + direction, direction)
    case '#':
      return False
    case _:
      return False
    
def moveAndPush(loc:Point, prevChar:str, direction:Point):
  whatIsThere = wideWarehouse[loc.x][loc.y]
  match whatIsThere:
    case '@':
      wideWarehouse[loc.x][loc.y] = '.'
      moveAndPush(loc+direction, whatIsThere, direction)

    case '.':
      wideWarehouse[loc.x][loc.y] = prevChar

    case '[':
      if (direction in [Point(0,1),Point(0,-1)]):
        # Pushing vertically, need to also push ] on RHS
        wideWarehouse[loc.x][loc.y] = prevChar
        wideWarehouse[loc.x+1][loc.y] = '.'

        moveAndPush(loc+direction, whatIsThere, direction)
        moveAndPush(loc+Point(1,0)+direction, ']', direction)
      else:
        # Pushing horizontally, push as normal
        wideWarehouse[loc.x][loc.y] = prevChar
        moveAndPush(loc+direction, whatIsThere, direction)

    case ']':
      if (direction in [Point(0,1),Point(0,-1)]):
        # Pushing vertically, need to also push [ on LHS
        wideWarehouse[loc.x][loc.y] = prevChar
        wideWarehouse[loc.x-1][loc.y] = '.'

        moveAndPush(loc+direction, whatIsThere, direction)
        moveAndPush(loc+Point(-1,0)+direction, '[', direction)
      else:
        # Pushing horizontally, push as normal
        wideWarehouse[loc.x][loc.y] = prevChar
        moveAndPush(loc+direction, whatIsThere, direction)


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
      justPickedUp = '@'
      currentSpace = robot
      warehouse[currentSpace.x][currentSpace.y] = '.'

      while justPickedUp != '.':
        newSpace = currentSpace + direction
        temp = warehouse[newSpace.x][newSpace.y]
        warehouse[newSpace.x][newSpace.y] = justPickedUp
        justPickedUp = temp
        currentSpace += direction
      robot += direction

  result = 0
  for x in range(len(warehouse)):
    for y in range(len(warehouse[x])):
      if warehouse[x][y] == 'O':
        result += x + (100 * y)
        
  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
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
          if len(wideWarehouse) == 0:
            for i in range(len(line.strip())*2):
              wideWarehouse.append(['#'])
          else:
            for i in range(0, len(line.strip())*2, 2):
              match line[i//2]:
                case '#':
                  wideWarehouse[i] += ['#']
                  wideWarehouse[i+1] += ['#']
                case '.':
                  wideWarehouse[i] += ['.']
                  wideWarehouse[i+1] += ['.']
                case 'O':
                  wideWarehouse[i] += ['[']
                  wideWarehouse[i+1] += [']']
                case '@':
                  wideWarehouse[i] += ['@']
                  wideWarehouse[i+1] += ['.']
            
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
    
    if canMove(wideWarehouse, robot, direction):
      moveAndPush(robot, '.', direction)
      robot += direction

  result = 0
  for x in range(len(wideWarehouse)):
    for y in range(len(wideWarehouse[x])):
      if wideWarehouse[x][y] == '[':
        result += x + (100 * y)
        
  return result


# Run the code for the specified part ----------------------------------
# answer = partOne("day15/test.txt")
# answer = partOne("day15/input.txt")

# answer = partTwo("day15/test.txt")
answer = partTwo("day15/input.txt")

pyperclip.copy(answer)
print(answer)
