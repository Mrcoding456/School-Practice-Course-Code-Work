def s(i):
    sum = 0
    for x in range (1, i+1):
        sum += x/(x+1)
    return sum

def main():
    print("\nEnter a positive integer: ", end ="")
    x = eval(input())
    while(x<= 0):
        x = eval(input("Enter a positive integer: "))

    print("\nWhen i =", x, ", the same series is", format(s(x), "0.3f"), ".")

main()