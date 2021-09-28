# Ask the user to enter a number
number = eval(input("Enter a number: "))
# If the number = x then print the following x---2x---3x---4x---5x
print(number, 2*number, 3*number, 4*number, 5*number, sep='---')