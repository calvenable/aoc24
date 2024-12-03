def validLevelTransition(a, b, shouldIncrease):
  if shouldIncrease and a > b:
    return False
  if not shouldIncrease and a < b:
    return False
  if abs(a - b) < 1:
    return False
  if abs(a - b) > 3:
    return False
  return True

def safeReport(report):
  shouldIncrease = report[1] > report[0]
  
  for i in range(len(report)-1):
    if not validLevelTransition(report[i], report[i+1], shouldIncrease):
      return False
  return True

def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  safeReports = 0

  for line in inputFile:
    report = list(map(int, line.split(' ')))
    if safeReport(report):
      safeReports += 1

  inputFile.close()
  print(safeReports)

def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")

  safeReports = 0

  for line in inputFile:
    report = list(map(int, line.split(' ')))
    if safeReport(report):
      safeReports += 1
    else:
      for problem in range(len(report)):
        popped = report.pop(problem)
        if safeReport(report):
          safeReports += 1
          break
        report.insert(problem, popped)

  inputFile.close()
  print(safeReports)

# partOne("day02/input.txt")
# partOne("input.txt")
partTwo("day02/input.txt")
# partTwo("input.txt")