def main():

    year, tuition = 0, 0

    print("Enter a year between  2000 and 2035: ", end="")
    year = eval(input())

    while (year<2000 or year > 2035):
        print("The year must be between 2000 and 2035. Enter the year again: ")
        year = eval(input())

    print("Enter the tuition for the year: ", end="")
    tuition = eval(input())

    while (tuition <= 0):
        print("Enter a positive tuition!!: ")
        tuition = eval(input())

    print("\t", "year", "\t\t$", "Tuition")
    print("-----------------------------")
# print the table showing the tuition for the next 10 years

    for x in range (1, 11):
        print("\t", year, "\t\t", format(tuition, "0.2f"))
        tuition += (tuition * 0.07)
        year += 1


main()