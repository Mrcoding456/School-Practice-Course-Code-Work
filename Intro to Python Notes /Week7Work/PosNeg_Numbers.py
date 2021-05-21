def main():
    neg_num = 0
    pos_num = 0
    average = 0
    total = 0
    integer = 0

    print("Enter an integer, enter 0 to exit: ", end="")
    integer = eval(input())

    total = total + integer

    if integer == 0:
        print("No numbers were entered except for 0.")

    while (integer != 0):
        if integer < 0:
            neg_num += 1
        elif integer > 0:
            pos_num += 1
        print("Enter an integer, enter 0 to exit:", end="")
        integer = eval(input())
        total = total + integer

    average = (total / (pos_num + neg_num))
    print("The number of positives is: ", pos_num)
    print("The number of negatives is: ", neg_num)
    print("The Total is ", total)
    print("The Average is ", format(average, "0.2f"))

main()
