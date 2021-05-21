myList = [1, 2, 3, 4, 5, 6]

for i in range (1, 6):

     myList[i-1] = myList[i]

for i in range (0, 6):

     print(myList[i], end ="  ")



xList = [1, 2, 3, 4]

x = 5

print(xList, + x)



list1 = [1, 2, 3]

list2 = []

for element in list1:

          list2.append(element)

list1 = [4, 5, 6]

print(list2)



xList =[1, 5, 5, 5, 5, 1]

max = xList[0]

indexOfMax = 0

for i in range(1, len(xList)):

      if (xList[i] > max):

        max = xList[i]
        indexOfMax = i

print(indexOfMax)

print(list2[3])
