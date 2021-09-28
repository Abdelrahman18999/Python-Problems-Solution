# Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, ..., 83, 86, 89.
for i in range(8, 90, 3):
    if i == 89:
        endchar = '.'
    else:
        endchar = ', '
    print(i, end= endchar)