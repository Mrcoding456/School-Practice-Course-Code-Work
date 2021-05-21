def ISBNCheck(first9digits):
    sum = 0
    for i in range(0, 9):
        if i == 0:
            sum += (i)*int(first9digits[i])
        else:
            sum += (i+1)*int(first9digits[i])

    x = sum % 11

    print("\nInside the ISBNcheck function:")
    print("d0 + 2d1+ 3d2 + 4d3 + 5d4 + 6d5 + 7d6 + 8d7 + 9d8 =", sum)
    print(sum,"% 11 =", x)

    if (x == 10):
        return first9digits + "x"
    else:
        return first9digits + str(1)


def main():
    first9digits = input("\nEnter the first 9 digits of an ISBN as a string: ")
    print("\nThe ISBN-10 number is", ISBNCheck(first9digits))

main()