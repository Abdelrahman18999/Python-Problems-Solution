# Write a program to print a hollow rectangle.
# Ask the user about the width and the length.
width = eval(input("Enter the width of the hollow rectangle: "))
length = eval(input("Enter the length of the hollow rectangle: "))
# Ask the user about which character he want to print the hollow rectangle with.
shapechar = input("Enter which character you want to print the rectangle with: ")
# Display
for i in range(width):
    if (i == 0) or (i == (width-1)):
        print(shapechar*length)
    else:
        print(shapechar, ' '*(length-2), shapechar , sep='')