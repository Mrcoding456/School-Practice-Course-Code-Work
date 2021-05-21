def main ():

    x = 0

    print("Enter an integer: ", end="")

    x = eval(input())
    check = x % 2 == 0

    print("Is", x, "an even:  ", check)

    print(check)

main()


