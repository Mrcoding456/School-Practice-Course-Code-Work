
def NameRepairing(name):


    for i in range(0,len(name)):
        if i == name[0]:
            name[0] = name[0].upper()
        if i == " ":
            name[i+1] = name[i+1:].upper()



    print("The repaired name: ", name)


def main():

    print("Enter a full name:")

    name = str(input())

    print(NameRepairing(name))


main()
