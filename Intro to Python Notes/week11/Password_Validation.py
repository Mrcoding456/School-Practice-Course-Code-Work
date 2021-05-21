
def isValidPassword(p):

    NumDigit, NumLetter =0, 0   #declare two local variables
    for x in range (0, len(p)): # i = 0, 1, 2, 3, ...,
        if (p[x].isdigit()==True):
            NumDigit += 1
        elif (p[x].isalpha()==True):
            NumLetter += 1
        print("\nThe password contains:")
        print(NumDigit, "numbers,", NumLetter, "letter(s), and it has",
len(p),"characters.")
    if NumDigit >= 1 and NumLetter >= 1 and len(p) >= 8:
        return True
    else:
        return False


def main():
    s = input("\nEnter a string for password: ")
    if isValidPassword(s):
        print("\nYes, it's a valid password", ".")
    else:
        print("\nNo, it's an invalid password", ".")

main()