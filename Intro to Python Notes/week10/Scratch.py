


def m(i):
    sum = 0
    for x in range(1, i + 1):
        sum = sum + x / (i - (x - 1))

    return sum


def main():
    print("Enter a positive integer: ", end="")
    i = eval(input())
    while (i <= 0):
        print("Input must be a positive. Enter the number: ", end="")


i = eval(input())

print("When i=", i, "the sum series m(", i, ")=", format(m(i), "0.4f"))

main()