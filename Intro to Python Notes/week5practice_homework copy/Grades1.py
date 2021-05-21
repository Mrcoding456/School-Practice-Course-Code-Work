def main():

    score, grade = 0, ""

    print("Enter a score between 0 and 100 inclusive: ")
    score = eval(input())

    if (score >= 90):
        grade = "A"
    elif (score >= 80):
        grade = "B"
    elif (score >= 70):
        grade = "C"
    elif (score >= 60):
        grade = "D"
    else:
        grade = "F"


    #find the grade based on the input score using an if...
    #for the instance, score = 72

    print("Your grade is", grade)

main()