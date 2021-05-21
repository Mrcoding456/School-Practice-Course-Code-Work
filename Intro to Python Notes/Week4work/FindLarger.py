def main ():
    x1, x2, larger = 0, 0, 0
    print("Enter two numbers:  ", end="")
    x1, x2 = eval(input())

    if (x1 > x2):
        print("the larger one is: ", x1)

    else:
        #print("The larger one is: ", x2)

    print("The larger one is: ", x1)
    larger = x1

main ()