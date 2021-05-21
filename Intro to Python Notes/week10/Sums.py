

def m(i):
    sumser = 0
    for x in range(1, i+1):
        sumser = sumser + x / (i - (x - 1))

    return(sumser)

def main():
    print("Enter a positive integer: ")
    i = eval(input())
    while(i <= 0):

        print("Input must be a positive integer. Enter the number: ")
        i = eval(input())
        x = i

    print("When i =", i,"the sum series m(", i,")=", format(m(i), "0.4f"))

main()