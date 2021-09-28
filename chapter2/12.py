# Write a program to print a triangle.
# Ask the user about how high the triangle should be.
hight = eval(input("How high the triangle should be?  "))
# Ask the user about which character he want to draw the triangle with.
shapechar = input("Which character you want to draw the triangle with?  ")
# Display
for i in range(1, hight+1):
    print(shapechar*i)