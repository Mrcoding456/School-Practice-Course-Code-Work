
def Doublecapacity(xList):

    zlist = [0]*len(xList)

    print("The original list is: ", xList)
    print("The expanded list is: ", xList + zlist)

def main():

    print("Enter some integers, separate each by spaces : ")

    ints = input()

    strList = ints.split()

    numlist = [eval(x) for x in strList]

    return Doublecapacity(numlist)

main()