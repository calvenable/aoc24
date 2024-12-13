# Advent of Code 2025 - day13
import pyperclip
from math import floor
from re import findall

def usefulFunction():
  return True


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  with open(inputFilePath, "r") as file:
    file_content = file.read()

  puzzleTextRegex = "Button A: X\\+(\\d+), Y\\+(\\d+)\\nButton B: X\\+(\\d+), Y\\+(\\d+)\\nPrize: X=(\\d+), Y=(\\d+)"
  matches = findall(puzzleTextRegex, file_content)

  result = 0
  for match in matches:
    (Xa, Ya, Xb, Yb, Xt, Yt) = list(map(int, match))
    try:
      b = ((Yt * Xa) - (Xt * Ya)) / ((Yb * Xa) - (Ya * Xb))
      a = (Xt - (b * Xb)) / Xa
    except ZeroDivisionError:
      continue
    
    if (floor(a) == a and floor(b) == b and a >= 0 and b >= 0 and a <= 100 and b <= 100):
      result += (3 * a) + b

  return int(result)


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  with open(inputFilePath, "r") as file:
    file_content = file.read()

  puzzleTextRegex = "Button A: X\\+(\\d+), Y\\+(\\d+)\\nButton B: X\\+(\\d+), Y\\+(\\d+)\\nPrize: X=(\\d+), Y=(\\d+)"
  matches = findall(puzzleTextRegex, file_content)

  result = 0
  for match in matches:
    (Xa, Ya, Xb, Yb, Xt, Yt) = list(map(int, match))
    Xt += 10000000000000
    Yt += 10000000000000
    try:
      b = ((Yt * Xa) - (Xt * Ya)) / ((Yb * Xa) - (Ya * Xb))
      a = (Xt - (b * Xb)) / Xa
    except ZeroDivisionError:
      continue
    
    if (floor(a) == a and floor(b) == b and a >= 0 and b >= 0):
      result += (3 * a) + b

  return int(result)


# Run the code for the specified part ----------------------------------
# answer = partOne("day13/test.txt")
# answer = partOne("day13/input.txt")

# answer = partTwo("day13/test.txt")
answer = partTwo("day13/input.txt")

pyperclip.copy(answer)
print(answer)
