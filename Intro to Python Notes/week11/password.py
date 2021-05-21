#Passwork Checking program#
# Check if a string p is a valid password
def isValidPassword(p):

    NumDigit, NumLetter, Upper = 0, 0, 0
    for x in range (0, len(p)):
        if p[x].isdigit()==True:
            NumDigit += 1
        elif p[x].isalpha()==True:
            NumLetter += 1
            if p[x].isupper()==True:
                Upper += 1
    print("\nThe password contains:")
    print(NumDigit, "number(s),", NumLetter, "letter(s) with", Upper, "uppercase(s), and it has",


len(p),"characters.")
    if NumDigit >= 1 and NumLetter >= 2 and len(p) >= 8 and Upper >= 1:
        return True
    else:
        return False


def main():
    s = input("\nEnter a string for password: ")
    if isValidPassword(s):
        print("\nIt's a valid password", ".")
    else:
        print("\nIt's an invalid password", ".")

main()