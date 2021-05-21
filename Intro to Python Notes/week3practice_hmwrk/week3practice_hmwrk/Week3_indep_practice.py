'''Chapter 4, Objects and Graphs'''


# Factorials!!!!

def main():
    fact = 1
    for factor in [5, 6, 7, 8, 9, 10, 11]:
        fact = fact * factor
    print(fact)


main()

def main():
    n = eval(input("Please Enter a Whole Number: "))
    fact = 1
    for factor in range(n, -1, 1):
        fact = fact * factor
    print("the factorial of", n, "is", fact)

main()

range = [5, 6, 7, 8, 9, 10, 11]
print(list(range))





