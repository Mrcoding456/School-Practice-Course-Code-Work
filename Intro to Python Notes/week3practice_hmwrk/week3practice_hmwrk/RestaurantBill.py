#RestaurantBill.py

#1 declare variables

'''mealcost, tip, tax, total = 0,0,0,0'''

#declare_named_constants

tiprate = 0.18
taxrate = 0.07

#2 get inputs

print("Enter the meal cost: ", end="")
mealcost = eval(input())
#3 Calculations

tip = (tiprate * mealcost) #18% tip rate
tax = (taxrate * mealcost) #7% tax rate
total = (mealcost + tax + tip)

#4 print the results

print("Bill Information: ")
print("\tMeal: \t$", format(mealcost, "0.2f"))
print("\tTip: \t$", format(tip, "0.2f"))
print("\ttax: \t$", format(tax, "0.2f"))
print("\tTotal: \t$", format(total, "0.2f"))

print("first line \n Second line")
print("\" Welcome to Python!! \"")






