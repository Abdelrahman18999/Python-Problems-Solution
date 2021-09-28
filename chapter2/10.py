# Write a program to print a rectangle with a custom character.
# Ask the user about the width and length of the rectangle.
length = eval(input("Enter the length of the rectangle: "))
width = eval(input("Enter the width of the rectangle: "))
# Ask the user about the character that he want to draw the rectangle with.
shapechar = input("Enter which character you want to draw the rectangle with: ")
# Display
for i in range(width):
    print(shapechar*length)