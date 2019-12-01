import math
filePtr = file("text")
values = filePtr.readlines()
total = 0
for value in values:
  current = value.strip("\n")
  integer = int(current)
  result = math.floor(integer/3) - 2
  while (result > 0):
    total += result
    result = math.floor(result/3) - 2
print total