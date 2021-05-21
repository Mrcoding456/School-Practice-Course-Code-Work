def main():

    import math

    RATE1, RATE2, RATE3, RATE4 = 2.50, 3.20, 4.50, 5.00
    W1, W2, W3, DIS = 2, 10, 30, 200

    print("Enter the package weight in kilograms (max 50 kg): ")
    weight = eval(input())
    print("Enter the distance the package is to be shipped (max 4000mi): ")
    distance = eval(input())

    instances = math.ceil(distance/200)


    if weight <= W1:
        rate = format(RATE1, "0.2f")
        ShippingCharge = RATE1 * instances
    elif weight <= W2:
        rate = format(RATE2, "0.2f")
        ShippingCharge = RATE2 * instances
    elif weight <= W3:
        rate = format(RATE3, "0.2f")
        ShippingCharge = RATE3 * instances
    else:
        rate = format(RATE4, "0.2f")
        ShippingCharge = RATE4 * instances

    print("Invoice Summary: ")
    print("\t The shipping rate is $", rate, "per 200 — miles shipped")
    print("\t There are", instances, "instances of 200 — mile blocks in", distance)
    print("\t Total =", instances, "X", rate, "=", format(ShippingCharge, "0.2f"))

main()