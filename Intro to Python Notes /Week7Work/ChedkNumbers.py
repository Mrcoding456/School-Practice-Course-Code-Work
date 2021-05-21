def main():

    x, evenNums, oddNums, sum = 0 , 0, 0, 0
    print("Enter an integer, enter 0 to exit: ", end="")
    x = eval(input())

    while(x != 0 ):
        check = (x % 2 == 0)

        if check == True:
            evenNums += 1
        else:
            oddNums += 1
        sum += x
        print("Enter an integer, enter 0 to exit: ", end="")
        x = eval(input())

    print("Even numbers = ", evenNums)
    print("Odd numbers = ", oddNums)
    print("Sum = ", sum)


main()