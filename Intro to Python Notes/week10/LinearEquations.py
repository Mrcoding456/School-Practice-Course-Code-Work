def isSolvable(a, b, c, d):
    if (a*d -b*c !=0):
        return True
    else:
        return False

def solution(a, b, c, d, p, q):
#find x =?, y = ?
    x =(p*d-b*q)/(a*d -b*c)
    y = (q*a-c*p)/(a*d -b*c)
    return x, y

def main():
    print("Enter a, b, c, d, p, q : ", end="")
    a, b, c, d, p, q =eval(input())

    if (isSolvable(a, b, c, d) == True):
        x, y = solution(a, b, c, d, p, q)
        print("The solution is: x =", x, ", y =", y)
    else:
        print("The system has no solution")