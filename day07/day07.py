# Advent of Code 2025 - day07
from functools import reduce

def canInsertOperatorsToSum(total, operands: list[int]):
  if len(operands) == 1:
    return operands[0] == total
  
  if (operands[0] + operands[1] <= total):
    reducedList = [operands[0] + operands[1]] + operands[2:]
    if (canInsertOperatorsToSum(total, reducedList)):
      return True
    
  if (operands[0] * operands[1] <= total):
    reducedList = [operands[0] * operands[1]] + operands[2:]
    if (canInsertOperatorsToSum(total, reducedList)):
      return True

  return False

def canInsertThreeOperatorsToSum(total, operands: list[int]):
  if len(operands) == 1:
    return operands[0] == total
  reducedList = []
  
  if (operands[0] + operands[1] <= total):
    reducedList = [operands[0] + operands[1]] + operands[2:]
    if (canInsertThreeOperatorsToSum(total, reducedList)):
      return True
    
  if (operands[0] * operands[1] <= total):
    reducedList = [operands[0] * operands[1]] + operands[2:]
    if (canInsertThreeOperatorsToSum(total, reducedList)):
      return True
    
  if (int(str(operands[0]) + str(operands[1])) <= total):
    reducedList = [int(str(operands[0]) + str(operands[1]))] + operands[2:]
    if (canInsertThreeOperatorsToSum(total, reducedList)):
      return True

  return False

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  operations = []
  for line in inputFile:
    result = int(line.split(':')[0])
    operands = list(map(int, line.strip().split(' ')[1:]))

    operation = (result, operands)

    operations.append(operation)

  inputFile.close()
  
  result = 0
  for operation in operations:
    if canInsertOperatorsToSum(operation[0], operation[1]):
      result += operation[0]

  print(result)


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")

  operations = []
  for line in inputFile:
    result = int(line.split(':')[0])
    operands = list(map(int, line.strip().split(' ')[1:]))

    operation = (result, operands)

    operations.append(operation)

  inputFile.close()
  
  result = 0
  for operation in operations:
    if canInsertThreeOperatorsToSum(operation[0], operation[1]):
      result += operation[0]

  print(result)

canInsertThreeOperatorsToSum
# Run the code for the specified part ----------------------------------
# partOne("day07/test.txt")
# partOne("day07/input.txt")

# partTwo("day07/test.txt")
partTwo("day07/input.txt")
