# Advent of Code 2025 - day03
import re

def getMatches(input):
  return re.findall("mul\((\d{1,3}),(\d{1,3})\)", input)


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  result = 0

  for line in inputFile:
    for match in getMatches(line):
      pairs = list(map(int, match))
      result += pairs[0] * pairs[1]

  inputFile.close()
  print(result)

# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")

  result = 0
  enabled = True

  for line in inputFile:
    searchIndex = 0
    lineSegment = line

    while (searchIndex < len(line)):
      lineSegment = line[searchIndex:]

      if (re.match("^do\(\)", lineSegment)):
        enabled = True
        searchIndex += 4
        continue

      if (re.match("^don't\(\)", lineSegment)):
        enabled = False
        searchIndex += 7
        continue

      if (enabled):
        enabledMulMatch = re.match("^mul\((\d{1,3}),(\d{1,3})\)", lineSegment)
        if (enabledMulMatch):
          result += int(enabledMulMatch[1]) * int(enabledMulMatch[2])
          searchIndex += len(enabledMulMatch[0])
          continue

      searchIndex += 1

  inputFile.close()
  print(result)


# Run the code for the specified part ----------------------------------
# partOne("day03/test.txt")
# partOne("day03/input.txt")

# partTwo("day03/test.txt")
partTwo("day03/input.txt")
