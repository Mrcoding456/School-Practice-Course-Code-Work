def gasCost (gasGrade, numberGallons):
    price, total, grade = 0, 0, ""
    Regular = 2.49
    Special = 2.79
    Super = 2.99


    if (gasGrade == "R"):
        price = 2.49
        grade = "Regular"
    elif (gasGrade == "S"):
        price = 2.79
        grade = "Special"
    else:
        price = 2.99
        grade = "Super"

    total = gasGrade*numberGallons

    print("You purchased", numberGallons, "gallons of ", grade, "grade gas at", price, "per gallon.")
    print("Your payment is", total)

def main():

    gasGrade = input(print("Enter a gas grade,\nR for Regular, S for Special, U for Super: "))
    while gasGrade != "R" or "U" or "S":
        print("Gas grade must be R, S, or U. Enter the gas grade. \nR for Regular, S for Special, U for Super: ")
        gasGrade = input("Gas grade must be R, S, or U. Enter the gas grade. \nR for Regular, S for Special, U for Super: ")




    print("Enter the number of gallons: ")
    numberGallons = eval(input())
    while (numberGallons <= 0):
        print("Number of gallons must be greater than 0. Enter the number of gallons: ")
        numberGallons = eval(input())

    gasCost(gasGrade, numberGallons)
main()

