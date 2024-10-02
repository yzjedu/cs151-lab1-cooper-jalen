# Programmers: [Your Name]
# Course: CS151, [Instructor's name]
# Due Date: 9/XX/2024
# Lab Assignment: 1
# Problem Statement: This program calculates the total cost of gas for a road trip
# Data In: Miles traveled, MPG of the vehicle, and cost per gallon of gas
# Data Out: The total cost for gas for the trip

# Get input from the user
miles = float(input("Enter the number of miles you will travel: "))
mpg = float(input("Enter the miles per gallon (MPG) of your vehicle: "))
price_per_gallon = float(input("Enter the price of gas per gallon: "))

# Calculate the total cost of the trip
total_cost = (miles / mpg) * price_per_gallon

# Output the result with two decimal places
print(f"The total cost for gas on your trip will be: ${total_cost:.2f}")