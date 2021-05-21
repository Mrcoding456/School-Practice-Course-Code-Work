def ElementShifter(xList):

    listresultList = []
    resultList  = []
    x1 = [0]
    resultList  = x1 + xList

def main():
    print("Enter some integers, separate each by spaces : ")

    s =input()

    strList = s.split()

    numList =[eval(x) for x in strList]

    print("\nThe list entered was: ", end="")

    print(numList)

    returnedList = ElementShifter(numList)

    print("The shifted list is: ", end="")

    print(returnedList)

main()