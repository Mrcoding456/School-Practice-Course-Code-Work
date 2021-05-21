def main ():

    bagels, total, cost = 0, 0, 0
    UNIT1, UNIT2, FIXEDNUM = 0.60, 0.75, 6

    print("Enter the number of bagels: ", end="")

    bagels = eval(input())

    #find unit cost using if/else
    if (bagels >= FIXEDNUM):
        total = bagels * 0.6
    else:
        cost = UNIT2

    total = bagels * 0.75
    print("Total =", bagels, "x $", cost, "= $", total)

main()