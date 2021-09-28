# Write a program to print the letter A with specified size from the user.
# Ask the user about the size (How large the letter?)
size = eval(input("Enter the size of the A letter or How long it should be? (NOTE -- Size must be an odd number)  "))
# Ask the user about the character that he want.
shapechar = input("Enter which the character you want to draw the letter A with: ")
# Display.
iteration = 0
orderLine = (size//2) +1
max = size + ((size-orderLine)*2)
for i in range(1, size*2, 2):
    iteration += 1
    spaces = (max - i) // 2
    numbershape = max - (spaces*2)
    if i == 1:
        print(spaces*' ', shapechar, spaces*' ', sep='')
    elif orderLine == iteration:
        print(spaces*' ', shapechar*i, spaces*' ', sep='')
    else:
        print(spaces*' ', shapechar, ' '*(numbershape-2), shapechar, spaces*' ', sep='')