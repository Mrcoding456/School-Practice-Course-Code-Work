def main():

    model, modelName, days, filltank, dailyCost, Total = "","", 0, "", 0, 0
    Cost1, Cost2, Cost3, Tank = 0,0,0,0

    print("Enter a vehicle model to rent \n W for Jeep Wrangler\n C for Jeep Grand Cherokee \n R for Land Rover --------:", end="")
    model1 = input() #Dont add eval bc it will convert to 0, somehow????

    print("Enter the number of days to rent: ", end="")
    days = eval(input())

    print("Fill up the tank (Y or N): ", end="")
    filltank = input()


    #find the model name using the input model
    if (model1 == "w" or "W"):
        modelName = "Jeep Wrangler"
        dailyCost = Cost1
    elif (model1 == "c" or "C"):
        modelName = "Jeep Grand Cherokee"
        dailycost = Cost2
    else:
        modelName = "Land Rover"
        dailyCost = Cost3


    print("\nCar Rental Information: ")
    print("\tVehicle Model:\t ", modelName)
    print("\tDaily Cost:\t\t", dailyCost)
    print("\tRental Days:\t ", days)

    if (filltank == "Y" or filltank == "y"):
        print("Fill Rank:\t\t", "Yes or No?????")
        Total = 1
    else:
        print("Fill Tank:\t\t", "No")
        Total =2
main()