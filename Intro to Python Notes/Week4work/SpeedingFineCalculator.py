def main():
    OVERLIMIT = 65
    OVERUNIT = 5
    OVERMPH = 90
    OVERPENALTY = 220
    DrivingSpeed = ""
    Fine = 0
    over90 = "No"
    print("Enter speed limit and clocked speed: ")
    limitSpeed, clockedspeed = eval(input())

    if limitSpeed >= clockedspeed:

        DrivingSpeed = "Legal"

    else:
        DrivingSpeed = "Illegal"
        Fine = (clockedspeed - limitSpeed) * OVERUNIT + OVERLIMIT

    if clockedspeed > OVERMPH :
        Fine = Fine + OVERPENALTY
        over90 = "Yes"

    print("the clocked speed is:",  DrivingSpeed)
    print("Driving over 90mph:", over90)
    print("The fine is: $", Fine)


main()
