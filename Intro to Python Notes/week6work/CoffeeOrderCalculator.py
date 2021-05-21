import math
import sys

def main():

    RATE1, RATE2, RATE3, RATE4, RATE5, RATE6, RATE7 = 0, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20
    BAG1, BAG2, BAG3, BAG4, BAG5, BAG6, BAG7 = 0, 25, 50, 100, 150, 200, 300
    BOX1, BOX2, BOX3 = 2.00, 1.50, 0.80


    print("Enter the amount number of bags ordered: ")
    numbags = eval(input())


    if numbags <= BAG1:
        print("Invalid Input! The number of bags must be greater than 0!")

        sys.out()


    large = math.floor(numbags//20)

    if ((numbags%20) // 10 == 1):
        medium = 1
    else:
        medium = 0

    if (numbags%10) // 5 <= 5:
            small = 1
    else:
            small = 2


    if (numbags >= 300):
        fprice = (numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3)
        dprice = RATE7 * ((numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3))
    elif (numbags >= 200):
        fprice = (numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3)
        dprice = RATE6 * ((numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3))
    elif (numbags >= 150):
        fprice = (numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3)
        dprice = RATE5 * ((numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3))
    elif (numbags >=100):
        fprice = (numbags*8.50)+(small*BOX3)+(medium*BOX2)+(large*BOX3)
        dprice = RATE4 * ((numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3))
    elif (numbags >= 50):
        fprice = (numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3)
        dprice = RATE3 * ((numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3))
    elif (numbags >= 25):
        fprice = (numbags * 8.50)+(small*BOX3)+(medium*BOX2)+(large*BOX3)
        dprice = RATE2*((numbags*8.50)+(small*BOX3)+(medium*BOX2)+(large*BOX3))
    else:
        fprice = (numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3)
        dprice = RATE1 * ((numbags * 8.50) + (small * BOX3) + (medium * BOX2) + (large * BOX3))


    print("Order Summary: ")
    print("\tBags Ordered: ", numbags,)
    print("\tFull Price: ", "x $8.50 = ", fprice)
    print("\t Discount: ", dprice)


    print("\n Box(es) used: ")
    if (large>=1):
        print("\t", large, "Large - $", (large*2.00))
    if (medium>=1):
        print("\t", medium, "Medium - $", (medium*1.50))
    if(small>=1):
        print("\t", small, "Small - $", (small*0.80))

main()















