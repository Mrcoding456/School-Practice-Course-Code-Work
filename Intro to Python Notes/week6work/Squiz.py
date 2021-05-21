import random

def main():
    x1= random.randint(1, 9)
    x2= random.randint(1, 9)

    if x1> x2:
        x1, x2 = x2, x1

    # Don't need to make an else statement



    print("what is", x1, "-", x2, "= ?", end="")
    userAns = eval(input())

    if(userAns == x1-x2):
        print("Correct!")
    else:
        print("Incorrect!!")
    print(x1, "-", x2, "=", x1-x2)

main()