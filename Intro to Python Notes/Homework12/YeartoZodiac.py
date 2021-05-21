def yeartozodiac(year):

    listzodiac = ["monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep"] #split the string monthName by comma into a list

    zodiac = year%12

    return listzodiac[zodiac]

def main():


    print("Enter a year:  ", end="")
    year = eval(input())

    while (year <= 0):
        print("The year must be a positive number. Enter the year: ", end="")
        year = eval(input())
    print("The year", year, "is the year of the", yeartozodiac(year), ".")

main()
