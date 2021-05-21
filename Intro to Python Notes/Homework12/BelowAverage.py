average = 0

def Belowavg(numlist):
    average = (sum(numlist)) / (len(numlist))
    print("The average of the numbers in the lost is: ", format(average, "0.2f"))
    print("All of the numbers in the list that are less than average are: ")
    for i in range(0, len(numlist)):  
        if (numlist[i] < average):
            print(numlist[i], end="  ")

def main():

    print("Enter some integers, separate each number by space in one line, then press enter: ")
    list = input()

    strlist = list.split()

    numlist = [eval(x) for x in strlist]

    if len(numlist) == 0:
        print("No numbers in the list.")
    else:
        print("\nYour input:", numlist)

    Belowavg(numlist)

main()
