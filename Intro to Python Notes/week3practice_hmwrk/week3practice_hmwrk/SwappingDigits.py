print("Enter an integer between 1 and 99: ")
num1 = eval(input())

num2 = (num1 // 10)
num3 = (num1 % 10)

swap = ((num3*10) + num2)
swap_times_two = (swap*2)

print("You entered", num1, ". The swapped integer is", swap, ".\nThe double of the swapped integer is: 2 x", swap, "=", swap_times_two)
