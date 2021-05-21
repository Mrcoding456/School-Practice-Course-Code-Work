def curvingGrades(rawList):

    print("\nRaw Scores:\t", end="")
    for i in range(0, len(rawList)):
        print("\t", rawList[i], end="\t")

    print()

    print("\nCurved Scores:\t", end="")
    for i in range(0, len(rawList)):

        curvedScore = (rawList[i])**(1 / 1.5)*(100**(1 - (1 / 1.5)))

        print(format(curvedScore, "0.2f"), end="\t")

    print()

def main():

    s = input("Enter some integer scores each between 0 and 100 inclusive, seperate each score by a space: \n")

    items = s.split()

    scores = [eval(x) for x in items]

    ret = (curvingGrades(scores))

    print(ret)

main()