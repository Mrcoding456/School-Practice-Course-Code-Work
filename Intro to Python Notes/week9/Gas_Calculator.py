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

    total = price * numberGallons

    print("You purchased", numberGallons, "gallons of", grade, "grade gas at $", price, "per gallon.")
    print("Your payment is $", format(total, "0.2f"))



def main():

    gasGrade = ""
    numberGallons = 0
    reg = str("R")
    sup = str("U")
    spec = str("S")


    print("Enter a gas grade,\nR for Regular, S for Special, U for Super: ")
    gasGrade = input()
    while gasGrade != reg and gasGrade != sup and gasGrade != spec:
        print("Gas grade must be R, S, or U. Enter the gas grade.\nR for Regular, S for Special, U for Super: ")
        gasGrade = input()

    print("Enter the number of gallons: ")
    numberGallons = eval(input())
    while (numberGallons <= 0):
        print("Number of gallons must be greater than 0. Enter the number of gallons: ")
        numberGallons = eval(input())

    z = gasCost(gasGrade, numberGallons)
main()

