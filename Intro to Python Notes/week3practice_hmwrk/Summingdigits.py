#1. Declare varibale

userIn, sum = 0, 0
rightD, leftD = 0, 0

#2 Getting the user inputs

print("Enter a number between 1 and 99 inclusive: ", end="")
userIn = eval(input())

#3 Calculations

rightD = userIn % 10
leftD = userIn // 10
sum = rightD + leftD

#4 Print the results
print("the sum is", sum)


