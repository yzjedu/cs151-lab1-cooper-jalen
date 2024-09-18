# Enter code here
# Read the README for instructions.
# You must write an algorithm and test cases first!

# Programmers:  Cooper Nazar and Jalen Henderson
# Course:  CS151, Professor Yalew
# Due Date: 9/18/2024
# Lab Assignment: 1
# Problem Statement: Calculates the cost of gas for a road trip.
# Data In: Miles traveled, miles per gallon of the car, and price of gas.
# Data Out: The cost of gas for the trip.

#Prompt user to input the values for miles, MPG, and gas price.
miles_traveled = int(input("How many miles will you travel? "))
miles_per_gallon = int(input("What is the miles per gallon of your vehicle? "))
gas_cost = float(input("What is the cost of gas? "))

#Calculate the total gas cost.
total_gas_cost = (miles_traveled / miles_per_gallon) * gas_cost

#Round total gas cost to two decimal places.
total_gas_cost = f'{total_gas_cost:.2f}'

#Output total gas cost.
print("The total gas cost for your trip is $", total_gas_cost)
