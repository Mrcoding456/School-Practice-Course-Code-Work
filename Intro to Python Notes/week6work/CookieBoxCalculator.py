import math
import sys

def main():
    # 1: declare variables
    bags, large, small, remainder = 0, 0, 0, 0

    # 2: Get user input
    print("Enter the number of bags: ", end="")
    bags = eval(input())

    if bags <=0:
        print("The number of bags must be positive. Try again!!")

        sys.out() # Fix


    # for instance, bags =20
    # find the number of large boxes used
    # Find the number of small boxes used

    large  = math.floor(bags//12)
    remainder = bags % 12
    if (remainder > 7):
        small = 2
    elif (remainder > 1):
        small = 1
    else:
        small = 0

    if (large > 0):
        print("\t\t", large, "lrge - $", large *2.50)
    if(small > 0):
        print("\t\t", small, "small - $", small*1.20)

    print("Box(es) Used: ")
    print("\t\t", large, " Large - $", large*2.50)
    print("\t\t", small, "Small - $", small*1.20)





main()