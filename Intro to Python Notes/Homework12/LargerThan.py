def LargerThan(numList, x):
    #print the numList
    if (len(numList) == 0):
        print("No numbers in the list.")
    else:
        print("\nThe input list is: ")
        for i in range(0, len(numList)):  #i =0, 1, 2, ..., len(numList)-1
            print(numList[i], end="  ")
            print()
            #find and print all of the numbers in the list that are greater than x
            print("\nAll of the numbers in the list that are greater than", x, "are: ")
            for i in range(0, len(numList)):  # i=0, 1, 2, ..., len(numList)-1
                if (numList[i] > x):
                    print(numList[i], end="  ")
def main():
#read numbers as a string from the user
    print("Enter some integers separated by spaces from one line, then press enter: ")
    s =input()

#split the input string by space, assign each split element to the

    strList = s.split() #convert each split element from string to number
    numList =[eval(x) for x in strList] #getting an integer input from the user
    print("Enter an integer: ", end="")
    x = eval(input()) #calling the LargerThan() function using the inputs
    LargerThan(numList, x)

main()