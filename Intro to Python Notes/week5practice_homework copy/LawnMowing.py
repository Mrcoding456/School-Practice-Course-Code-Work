def main():

    FEE1 = 25
    FEE2 = 35
    FEE3 = 50
    SER1 = 0
    SER2 = 5
    SER20 = 3
    SIZE1 = 400
    SIZE2 = 600

    print("Enter the lot size in square feet: ")
    lotsize = eval(input())
    print("Enter the number of times today the bill for the season: ")
    payQ = eval(input())
    print("1 for once")
    print("2 for twice")
    print("20 for 20 times-----", payQ)

    if lotsize < SIZE1:
        weeklyfee = FEE1
    elif lotsize <= SIZE2:
        weeklyfee = FEE2
    else:
        weeklyfee = FEE3


    if payQ <= 1:
        servicechrg = SER1
        total = SER1 + weeklyfee*20
        PPA = total
    elif payQ <= 2:
        servicechrg = SER2
        total = (2*SER2) + (weeklyfee*20)
        PPA = (total / 2)
    else:
        servicechrg = SER20
        total = (20*SER20) + (weeklyfee*20)
        PPA = (total / 20)

    print("Lawn Mowing Information: ")
    print("\t The Lot Size: \t\t\t\t\t", lotsize , "Sq Ft")
    print("\t Number of Payments: \t\t\t", payQ, "times")
    print("\t Weekly Mowing Fee: \t\t\t", format(weeklyfee, "0.2f"))
    print("\t Service Charge Per Payment: \t", format(servicechrg, "0.2f"))
    print("\t Per Payment Amount: \t\t\t", format(PPA, "0.2f"))
    print("Total = $", PPA, "x", payQ, "=", total)

main()