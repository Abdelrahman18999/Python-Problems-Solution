# Write a program to fill the screen horizontly and vertically with your name.
# Say i will fill it by 6 x 10.
# First take the name from the user.
name = input("Enter your name: ")
for i in range(10):
    print((name+' ')*6)