import math

def isValid(s1, s2, s3):
    if (s1+s2>s3 and s3+s2>s1 and s3+s1>s2):
        return True
    else:
        return False

def solution(s1, s2, s3):
    s = ((s1+s2+s3)/2)
    localvar1 = s*(s-s1)*(s-s2)*(s-s3)
    Area = math.sqrt(localvar1)
    Para = s1+s2+s3
    print("The area of the triangle is", format(Area, "0.2f"), "square inches.")
    print("The perimeter of the triangle is", format(Para, "0.2f"), "inches.")
    return Area, Para

def main():
    print("Enter three sides for a triangle in inches: ")
    s1, s2, s3 = eval(input())
    while(isValid(s1, s2, s3) == False or s1<0 or s2<0 or s3<0):
        print("Invalid input! Please enter the three sides: ")
        s1,s2,s3 = eval(input())
    solution(s1,s2,s3)

main()