import random

def main():
    x1= random.randint(1, 9)
    x2= random.randint(1, 9)

    rp1 = random.randint(1,4)
    rp2 = random.randint(1,4)

    print("what is", x1, "x", x2, "= ?", end="")
    userAns = eval(input())

    if(userAns == x1*x2):
            if rp1 == 1:
                print("\nExcellent!")
            elif rp1==2:
                print("\nKeep up the good work!")
            elif rp1==3:
                print("\nNice work!")
            else:
                print("\nVery good!")
    else:
        if rp2 == 1:
            print("\nNo, but thanks for trying.")
        elif rp2 == 2:
            print("\nClose, but not quite right.")
        elif rp2 == 3:
            print("\nWrong answer.")
        else:
            print("\nNo, but it's okay to be wrong.")
    print(x1, "x", x2, "=", x1*x2)

main()