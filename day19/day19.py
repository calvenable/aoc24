# Advent of Code 2025 - day19
import pyperclip
import re

canMakeMemory:dict[str, bool] = dict()

def canMake(pattern:str, towelOptions:list[str]):
  if pattern not in canMakeMemory:
    canMakeMemory[pattern] = checkCanMake(pattern, towelOptions)
  return canMakeMemory[pattern]
  
def checkCanMake(pattern:str, towelOptions:list[str]):
  if (pattern == ''):
    return True
  
  for option in towelOptions:
    m = re.match(option, pattern)
    if (m is not None and canMake(pattern[m.span()[1]:], towelOptions)):
      return True
  return False


howManyOptionsMemory:dict[str, int] = dict()

def howManyOptions(pattern:str, towelOptions:list[str]):
  if pattern not in howManyOptionsMemory:
    howManyOptionsMemory[pattern] = countHowManyOptions(pattern, towelOptions)
  return howManyOptionsMemory[pattern]
  
def countHowManyOptions(pattern:str, towelOptions:list[str]):
  if (pattern == ''):
    return 1
  
  waysToMakeChildren = 0
  for option in towelOptions:
    m = re.match(option, pattern)
    if (m is not None):
      waysToMakeChildren += howManyOptions(pattern[m.span()[1]:], towelOptions)

  return waysToMakeChildren




# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):

  towelOptions = []
  patternsToMake = []
  count = 0
  with open(inputFilePath, "r") as file:
    for line in file:
      if (count == 0):
        towelOptions = line.strip().split(', ')
      elif (count > 1):
        patternsToMake.append(line.strip())
        
      count += 1

  result = 0
  for pattern in patternsToMake:
    if (canMake(pattern, towelOptions)):
      result += 1

  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  towelOptions = []
  patternsToMake = []
  count = 0
  with open(inputFilePath, "r") as file:
    for line in file:
      if (count == 0):
        towelOptions = line.strip().split(', ')
      elif (count > 1):
        patternsToMake.append(line.strip())
        
      count += 1

  result = 0

  for pattern in patternsToMake:
    if (canMake(pattern, towelOptions)):
      result += howManyOptions(pattern, towelOptions)

  return result


# Run the code for the specified part ----------------------------------
# answer = partOne("day19/test.txt")
# answer = partOne("day19/input.txt")

# answer = partTwo("day19/test.txt")
answer = partTwo("day19/input.txt")

pyperclip.copy(answer)
print(answer)
