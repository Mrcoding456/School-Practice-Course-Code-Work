def avgtwohighest(s1, s2, s3):
    average = 0

    if (s1<s2 and s1<s3):
        average = (s2+s3)/2

    elif (s2<s1 and s2<s3):
        average = (s1+s3)/2

    else:
        average = (s1+s2)/2

    return average

def main():
    print("Enter three scores between 0 and 100 inclusive:")
    s1, s2, s3 = eval(input())

    average2 = avgtwohighest(s1, s2, s3)
    print("The average of the two highest scores is: " + format(average2, "0.2f"))

main()