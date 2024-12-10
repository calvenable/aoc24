# Advent of Code 2025 - [DAY]
import pyperclip

def usefulFunction():
  return True


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  for line in inputFile:
    if usefulFunction():
      print(line)

  inputFile.close()
  result = 0


  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  return False


# Run the code for the specified part ----------------------------------
answer = partOne("[DAY]/test.txt")
# answer = partOne("[DAY]/input.txt")

# answer = partTwo("[DAY]/test.txt")
# answer = partTwo("[DAY]/input.txt")

pyperclip.copy(answer)
print(answer)