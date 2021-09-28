# Ask the user to enter the price of the meal then ask him about the percent tip he want to leave.
mealPrice = eval(input("Enter the meal price: "))
tipPercent = eval(input("Enter the tip percent you want to leave: "))/100
# Calculate how much the tip and the total bill with the tip included.
tip_amount = mealPrice*tipPercent
totalBill = mealPrice + tip_amount
# Display total bill
print("Your total bill worth", totalBill, "$.")
