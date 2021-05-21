
print("Enter the pounds of cookies you want to order: ", end="")

pounds = eval(input())
shippingpp = 0.85
overhead = 1.75
costperpound = 5.50

costofpounds = pounds * costperpound
shipping = ((shippingpp * pounds) + overhead)
total = shipping + costofpounds

print("Payment information: ")
print("\tCost of cookies: \t$", format(costofpounds, "0.2f"))
print("\tShipping Fee:    \t$", format(shipping, "0.2f"))
print("\tTotal Due:       \t$", format(total, "0.2f"))



