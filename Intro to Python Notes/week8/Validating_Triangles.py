import math

def main():

    a, b, c = 0, 0, 0

    print("Enter three edges for a triangle in inches: ")
    a, b, c = eval(input())

    while (a+b < c or c+a < b or b+c < a):
        print("No, the three edges can't form a triangle. ")
        print("\nEnter three edges for a triangle in inches: ")
        a, b, c = eval(input())

    else:
        s = (a+b+c)/2
        inputa = s*(s-a)*(s-b)*(s-c)
        area = math.sqrt(inputa)
        print("Yes, the three edges can form a triangle")
        print("the area of the triangle is ", format(area, "0.2f"))

main()



