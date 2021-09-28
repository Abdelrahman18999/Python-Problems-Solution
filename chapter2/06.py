# Write a program that uses a for loop to print the numbers 100, 98, 96, ..., 4, 2.
for i in range(100, 1, -2):
    if i == 2:
        endchar = '.'
    else:
        endchar = ', '
    print(i, end=endchar)
    