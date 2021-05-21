def NameRepairing(name):


    for i in range(0, len(name)):

        if i == name[0]:
            name[i] = name[0].upper()

        elif (name[i] == ' '):
            i += name[i + 1].upper()

        else:
            name[i] += name[i]


    print("The repaired name: ", id)


def main():

    print("Enter a full name:")

    name = str(input())

    print(NameRepairing(name))


main()
