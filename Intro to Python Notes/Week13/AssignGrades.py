def assignGrades(scoreList):


    best = max(scoreList)

    print("\nScores:\t", end="")

    for i in range(0, len(scoreList)):
        print(scoreList[i],end="\t")

    print()

    grades = [0]*len(scoreList)

    print("Grades:\t", end="")

    for i in range(0, len(scoreList)):
        if scoreList[i] >= best - 10:
            grades[i] = 'A'
        elif scoreList[i] >= best - 20:
            grades[i] = 'B'
        elif scoreList[i] >= best - 30:
            grades[i] = 'C'
        elif scoreList[i] >= best - 40:
            grades[i] = 'D'
        else:
            grades[i] = 'F'

        print(grades[i], end="\t")

def main():
    print("\n")

    s = input("Enter some scores, separate each number by space in one line: \n")

    items = s.split()
    scores = [ eval(x) for x in items ]
    assignGrades(scores)
    print("\n\n")

main()