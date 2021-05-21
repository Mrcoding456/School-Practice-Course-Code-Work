def ISBNCheck(s):
    sum = 0
    for i in range(0, 12):        # i = 0, 1, 2, 3, ..., 11
        if (i % 2 == 0):        # i is an even, i = 0, 2, 4, 6, 8, 10
            sum += int(s[i])  #sum = s[0] + s[2] + s[4] + s[6] + s[8] + s[10]

        else:                         # i is an odd, i = 1, 3, 5, 7, 9, 11sum
            sum += 3*int(s[i])

        x = 10 - sum % 10

        print("\nInside the ISBNcheck function:")
        print("d0 + 3d1+ d2 + 3d3 + d4 + 3d5 + d6 + 3d7 + d8 + 3d9 + d10 + 3d11 =", sum)
        print("10 -", sum, "% 10 =", x)

        if (x == 10):
            return s + str(0)
        else:
            return s + str(x)

def main():
            ISBNfirst12 = input("\nEnter the first 12 digits of an ISBN as a string: ")
            print("\nThe ISBN-13 number is", ISBNCheck(ISBNfirst12))

main()