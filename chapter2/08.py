# Ask the user for his name.
name = input("Enter your name: ")
# Ask the user how many times he want to print his name.
times = eval(input("How many times you want to print your name: "))
# Ask the user if he want to print his name vertical or horizontal
VorH = input("If you want to print it vertical enter v. IF you want it horizontal enter h: ")
# Display
if VorH == 'v':
    endchar = '\n'
elif VorH == 'h':
    endchar = ' '
for i in range(times):
    print(name, end= endchar)