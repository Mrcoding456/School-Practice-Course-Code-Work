def ConstructID(name, address):
    id = name[0]
    for i in range (0, len(name)):
        if (name[i] == ' '):
            id += name[i+1]

    x = address.find(" ")  #x is index of the first space in address
    for i in range (0, x): # i=0, 1, 2, ..., x-1
        id += address[i]  #adding all characters before the first space in address to id
        return id.upper()

def main():
        print("Enter your full name: ", end="")
        name = input()
        print("Enter your complete address: ", end="")
        address = input("")
        print("\nYour ID is", ConstructID(name, address))

main()