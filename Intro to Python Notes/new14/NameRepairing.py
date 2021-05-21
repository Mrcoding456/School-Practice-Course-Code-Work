def NameRepairing(name):

    name1 = name[0].upper()


    for i in range(0,len(name)-1):

        if name[i] ==' ':

            name1 += name[i+1].upper()
        else:
            name1 += name[i+1].lower()


    return name1

def main():

    print("Enter a full name:")
    name =input()
    print("The repaired name: ", NameRepairing(name))

main()