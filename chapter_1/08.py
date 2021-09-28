# Ask the user to enter three numbers (Use three seperate input statments).
number1 = eval(input("Enter the first number:"))
number2 = eval(input("Enter the second number:"))
number3 = eval(input("Enter the third number:"))
# Calculate total and average of these three numbers.
total = number1 + number2 + number3
average = total / 3
# Display the total and the average.
print("The total of the three numbers you entered =", total)
print("The average of the three numbers you entered =", average)