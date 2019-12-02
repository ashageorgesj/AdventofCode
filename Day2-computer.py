#import math
import copy
def change(myList,value1,value2):
  myList[1] = value1
  myList[2] = value2
  i = 0
  while i < len(myList):
    if myList[i] == '1':
      first = int(myList[i + 1])
      second = int(myList[i + 2])
      result = int(myList[i + 3])
      myList[result] = str(int(myList[first]) + int(myList[second]))
    elif myList[i] == '2':
      first = int(myList[i + 1])
      second = int(myList[i + 2])
      result = int(myList[i + 3])
      if result > len(myList):
        break
      myList[result] = str(int(myList[first]) * int(myList[second]))
    elif myList[i] == '99':
      break
    i = i + 4
  if int(myList[0]) == 19690720:
    print value1,value2
    print myList[0]
    print 100*int(value1) + int(value2)
  
fileptr = file("text")
input = fileptr.readlines()
values = input[0].split(",")
values[1] = '12'
values[2] = '2'
for j in range(13,99):
  for k in range(3,99):
    new = copy.copy(values)
    change(new,str(j),str(k))

