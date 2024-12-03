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


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  return False


# Run the code for the specified part ----------------------------------
partOne("[DAY]/test.txt")
# partOne("[DAY]/input.txt")

# partTwo("[DAY]/test.txt")
# partTwo("[DAY]/input.txt")