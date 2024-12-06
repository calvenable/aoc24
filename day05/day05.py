# Advent of Code 2025 - day05

def inOrder(update, orderings):
  # Update: [75,47,61,53,29]
  # Orderings: {47: [29,12,75]}
  encountered = []
  for page in update:
    encountered.append(page)
    if (page in orderings):
      for afterPage in orderings[page]:
        if (afterPage in encountered):
          return False
  return True

def reorderUpdate(update: list[str], orderings: dict[str, list[str]]):
  count = 0
  encountered = []
  end = []

  while (count < len(update)):
    el = update[count]
    if (el not in orderings):
      end.append(update.pop(count))
      continue

    rulesToGetBehind = [x for x in encountered if x in orderings[el]]
    encountered.append(el)

    if (rulesToGetBehind):
      moveTo = min(map(lambda n: update.index(n), rulesToGetBehind))
      update.insert(moveTo, update.pop(count))
    count += 1

  return update + end


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  inputFile = open(inputFilePath, "r")

  orderings = dict()
  updates = []

  firstSection = True
  for line in inputFile:
    line = line.strip()
    if (firstSection):
      if (line == ''):
        firstSection = False
        continue

      if (line.split('|')[0] not in orderings):
        orderings[line.split('|')[0]] = [line.split('|')[1]]
      else:
        orderings[line.split('|')[0]].append(line.split('|')[1])

    else:
      updates.append(line.strip().split(','))

  inputFile.close()
  
  middlePageSum = 0
  for update in updates:
    if (inOrder(update, orderings)):
      middlePageSum += int(update[len(update)//2])

  print(middlePageSum)


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  inputFile = open(inputFilePath, "r")

  orderings = dict()
  updates = []

  firstSection = True
  for line in inputFile:
    line = line.strip()
    if (firstSection):
      if (line == ''):
        firstSection = False
        continue

      if (line.split('|')[0] not in orderings):
        orderings[line.split('|')[0]] = [line.split('|')[1]]
      else:
        orderings[line.split('|')[0]].append(line.split('|')[1])

    else:
      updates.append(line.strip().split(','))

  inputFile.close()
  
  middlePageSum = 0
  for update in updates:
    if (not inOrder(update, orderings)):
      # Put them in order and then take the middle sum
      reorderedUpdate = reorderUpdate(update, orderings)
      middlePageSum += int(reorderedUpdate[len(update)//2])

  print(middlePageSum)


# Run the code for the specified part ----------------------------------
# partOne("day05/test.txt")
# partOne("day05/input.txt")

# partTwo("day05/test.txt")
partTwo("day05/input.txt")
