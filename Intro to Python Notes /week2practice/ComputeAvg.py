#This program reads three numbers from the user
#the program displays the average on the screen

#step 1: Declare variables
num1, num2, num3, avg = 0, 0, 0, 0
'''num2 = 0
num3 = 0
avg = 1'''

#step 2: getting the inputs

print("Enter the first number: ", end='')
num1 = eval(input())
print("Enter the second number: ", end='')
num2 = eval(input())
print("Enter the third number: ", end='')
num3 = eval(input())

#step 3: making calculations

avg = (num1+num2+num3)/3

#step 4: display the result

print("The average of:", num1, ",", num2,", and",num3, "is", avg)