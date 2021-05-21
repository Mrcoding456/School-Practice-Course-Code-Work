def main():

    year, population = 0,0

    print("Enter a year after 2010: ")
    year = eval(input())

    while (year < 2010):
        print("Year must be greater than 2010. Enter a year: ")
        year = eval(input())

    pop_2010 = 308.746

    print("\t\t Year", "\t\t Population")
    print("---------------------------------------------------")

    yearexact = year+1

    for year in range (2010, yearexact):
        print("\t\t", year, "\t\t", format(pop_2010, "0.3f"))
        pop_2010 = pop_2010 + (pop_2010*0.0069)


main()