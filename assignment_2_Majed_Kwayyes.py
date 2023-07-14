def countDigits(n):
  if (n // 10 == 0):
    return 1
  else:
    return 1 + countDigits(n // 10)


def findMax(lst):
  if len(lst) == 1:
    return lst[0]
  else:
    max_rest = findMax(lst[1:])
    return max_rest if max_rest > lst[0] else lst[0]


def terminateProgram():
  return


def displayChoices():
  print("1. Count Digits\n" + "2. Find Max\n" + "3. Count Tags\n" + "4. Exit")


def main():
  displayChoices()


choice = int(input("please enter your choice here: "))

while (choice != 4):
  if (choice == 1):
    print(countDigits(3212222))
  elif (choice == 2):
    print(findMax([1, 2, 3, 4, 6, 10]))
  #elif(choice == 3):
  #countTags()
  elif (choice == 4):
    terminateProgram()
  else:
    print("Invalid number, please choose a number from the choices above")

  main()
