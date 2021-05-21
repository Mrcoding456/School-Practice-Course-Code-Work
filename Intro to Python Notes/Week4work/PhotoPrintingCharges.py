def main():
    print("Enter the number of copies: ", end="")
    copies = eval(input())
    COST1 = 6.25
    COST2 = 5.00
    FIXEDCOPY = 20

    if (copies <= FIXEDCOPY):
        total = (copies * COST1)
        print("You made", copies, "copies.")
        print("Total =", copies, "x $6.25 = $", format(total, "0.2f"))

    else:
        total = (FIXEDCOPY * COST1) + (copies - FIXEDCOPY) * COST2
        variablecopy = (copies - FIXEDCOPY)

        print("You made", copies, "copies.")
        print("Total =  ( 20 x $6.25 ) + (", variablecopy, "x $5.00 ) = $", format(total, "0.2f"))

main()