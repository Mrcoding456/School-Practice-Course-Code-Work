import math
import sys

def main():

    RATE1, RATE2, RATE3, RATE4, RATE5, RATE6, RATE7 = 0, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20
    BAG1, BAG2, BAG3, BAG4, BAG5, BAG6, BAG7 = 0, 25, 50, 100, 150, 200, 300
    BOX1, BOX2, BOX3 = 2.00, 1.50, 0.80


    print("Enter the number of bags ordered: ")
    numbags = eval(input())


    if numbags <= BAG1:
        print("Invalid Input! The number of bags must be greater than 0!")

        sys.out()


    large = math.floor(numbags//20)


    if ((numbags%20) // 10 == 1):
        medium = 1
    else:
        medium = 0
    if ((numbags%10) // 5 >= 1):
        small = 2
    else:
        small = 1


    cof_b = (large*BOX1 + medium*BOX2 + small*BOX3)


    if (numbags >= 300):
        fprice = (numbags * 8.50)
        discount = RATE7 * fprice
        prcoff = "(20.00% off)"
        tprice = fprice - (RATE7 * fprice) + cof_b
    elif (numbags >= 200):
        fprice = (numbags * 8.50)
        discount = RATE6 * fprice
        prcoff = "(15.00% off)"
        tprice = fprice - (RATE6 * fprice) + cof_b
    elif (numbags >= 150):
        fprice = (numbags * 8.50)
        discount = RATE5 * fprice
        prcoff = "(12.00% off)"
        tprice = fprice - (RATE5 * fprice) + cof_b
    elif (numbags >=100):
        fprice = (numbags*8.50)
        discount = RATE4 * fprice
        prcoff = "(10.00% off)"
        tprice = fprice - (RATE4 * fprice) + cof_b
    elif (numbags >= 50):
        fprice = (numbags * 8.50)
        discount = RATE3 * fprice
        prcoff = "(8.00% off)"
        tprice = fprice - (RATE3 * fprice) + cof_b
    elif (numbags >= 25):
        fprice = (numbags * 8.50)
        discount = RATE2*fprice
        prcoff = "(5.00% off)"
        tprice = fprice - (RATE2*fprice) + cof_b
    else:
        fprice = (numbags * 8.50)
        discount = RATE1 * fprice
        prcoff = "(0.00% off)"
        tprice = fprice - (RATE1 * fprice) + cof_b


    print("\nOrder Summary: ")
    print("\tBags Ordered: \t", numbags)
    print("\tFull Price: \t", numbags, "x $8.50 = ", "$", format(fprice, "0.2f"))
    print("\tDiscount: \t\t", "$", format(discount, "0.2f"), prcoff)
    print("\n\tBox(es) used: ")
    if (large>=1):
        print("\t\t\t\t\t", large, "Large - $", format((large*BOX1), "0.2f"))
    if (medium>=1):
        print("\t\t\t\t\t", medium, "Medium - $", format((medium*BOX2), "0.2f"))
    if(small>=1):
        print("\t\t\t\t\t", small, "Small - $", format((small*BOX3), "0.2f"))

    print("\nTOTAL =", "$", fprice, "-", "$", discount, "+", "$", format(cof_b, "0.2f"), "=", "$", format(tprice, "0.2f"))


main()