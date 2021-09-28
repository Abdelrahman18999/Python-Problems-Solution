# Write a program to print Fibonacci numbers which sequence is below and ask the user how many number he want to display from these sequences
# 1,1,2,3,5,8,13,21,34,55,89,....

# Ask the uer how many numbers he want
items = eval(input("How many number you want from Fibonacci series? "))
# Display
holder = 1
FN = 1
for i in range(1, items+1):
    if i <= 2:
        FN = i + (i-1)
        print(FN, end=', ')
    else:
        Before = FN
        holder = Before
        FN += Before
        print(FN, end=', ')
        Before = FN
        