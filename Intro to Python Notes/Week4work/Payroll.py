# payroll.py

def main():
    hours, payrate, regular, overtime, gross = 0, 0, 0, 0, 0
    HOURS, OVERRATE = 40, 1.5
    overworked = "no"
    print("Enter the amount of hours you worked and pay rate: ", end="")
    hours, rate = eval(input())

    # find regular and overtime using an if ... else

    if (hours >= 40):  # for instance, hours = 45
        regular = 40 * rate
        overtime = ((hours - HOURS) * rate * OVERRATE)
        overworked = "Yes"
    else:
        regular = (hours * rate)
        overtime = 0
        overworked = "No"
    gross = regular + overtime
    print("Worked overtime; ", overworked)
    print("Regular ", regular)
    print("Overtime", overtime)
    print("Gross", gross)


main()
