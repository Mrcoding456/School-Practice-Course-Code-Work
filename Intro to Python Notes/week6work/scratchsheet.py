import math

print("Enter bags: ")
numbags = eval(input())

large = math.floor(numbags//20)

if ((numbags % 20) // 10 == 1):
    medium = 1
else:
    medium = 0

if (numbags % 10) // 5 <= 5:
    small = 1
else:
    small = 2

print(large)
print(medium)
print(small)