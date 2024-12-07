# Advent of Code 2025 - [DAY]

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
print(partOne("[DAY]/test.txt"))
# print(partOne("[DAY]/input.txt"))

# print(partTwo("[DAY]/test.txt"))
# print(partTwo("[DAY]/input.txt"))