import math

def main():




    print("Enter the hours parked: ")
    hours = eval(input())

    if (hours <= 2):
        charge = 2
    else:
        charge = (2 + math.ceil((hours - 2)) * 1.5)
        if (charge >= 10):
            charge = 10
    print("Your parked", math.ceil(hours), "hours.")
    print("Charge = $", format(charge, "0.2f"))


main()