def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  list1 = []
  list2 = []

  for line in inputFile:
    lineElements = line.strip().split(' ')
    list1.append(int(lineElements[0]))
    list2.append(int(lineElements[-1]))
  inputFile.close()

  list1.sort()
  list2.sort()

  result = 0

  for num in range(len(list1)):
    result += abs(list1[num] - list2[num])

  print(result)

def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")

  list1 = []
  list2 = dict()

  for line in inputFile:
    lineElements = line.strip().split(' ')

    num1 = int(lineElements[0])
    list1.append(num1)
    if (num1 not in list2):
      list2[num1] = 0

    num2 = int(lineElements[-1])
    if (num2 in list2):
      list2[num2] += 1
    else:
      list2[num2] = 1

  inputFile.close()

  result = 0

  for num in range(len(list1)):
    result += list1[num] * list2[list1[num]]

  print(result)

partTwo("day01/input.txt")
