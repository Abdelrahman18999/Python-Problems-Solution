# Write a program to print an upside down triangle.
# Ask the user about how long the triangle should be?
hight = eval(input("How long the triangle should be?  "))
# Ask the user about the character shape.
shapechar = input("Which character you want to print the triangle with?  ")
# Display.
for i in range(hight, 0, -1):
    print(shapechar*i)