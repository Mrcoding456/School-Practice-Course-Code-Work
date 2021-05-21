# MonthNames program
def monthName(x):
    monthName = "January,February,March,April,May,June,July,August,September,October,November,December"#split the string monthName by comma into a list

    monthNameList = monthName.split(",")
    return monthNameList[x-1]

def main():
#get a user input between 1 and 12
    print("Enter a number between 1 - 12:  ", end="")
    number = eval(input())

    while (number >12 or number <1):
        print("Enter a number between 1 and 12: ", end="")
        number = eval(input())
        print("\nYou entered", number, ". The month name is", monthName(number), ".")

    main()