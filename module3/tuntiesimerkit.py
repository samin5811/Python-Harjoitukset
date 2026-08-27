# Tuntiesimerkit Module 3

# 1

import math

# square_side = float(input("Give me the side length of a square: "))
# circle_radius = float(input("Give me the radius of a circle: "))

# area_of_square = square_side ** 2
# area_of_circle = math.pi * circle_radius * circle_radius

# print("Area of the square = " + str(area_of_square))
# print("Area of the circle = " + str(area_of_circle))

# 2

# banana_in_kg = float(input("Give me the weight of bananas in kg: "))
# apple_in_kg = float(input("Give me the weight of apples in kg: "))
# orange_in_kg = float(input("Give me the weight of oranges in kg: "))

# banana_price = banana_in_kg * 2.85
# apple_price = apple_in_kg * 3.15
# orange_price = orange_in_kg * 4.05
# fruits_total_price = banana_price + apple_price + orange_price

# print("\nbanana price is " + str(banana_price) + "€")

# print("\napple price is " + str(apple_price) + "€")

# print("\norange price is " + str(orange_price) + "€")

# print("\nTotal price is " + str(fruits_total_price) + "€")

# print(f"\nbanana price is {banana_price:.2f}€")
# print(f"\napple price is {apple_price:.2f}€")
# print(f"\norange price is {orange_price:.2f}€")
# print(f"\nTotal price is {fruits_total_price:.2f}€")

# 3

import random



while True:
    user_input = input("\nDo you want to roll the dice? (y/n): ")
    if user_input.lower() == "y":
        dice1_number = random.randint(1, 6)
        dice2_number = random.randint(1, 20)
        print("Exiting the program.")
        print("\nDice 1 is " + str(dice1_number))
        print("Dice 2 is " + str(dice2_number))
        print("Total number is " + str(dice1_number + dice2_number))
        continue
    else:
        break

# input("Press enter to roll the dice...")

# dice1_number = random.randint(1, 6)
# dice2_number = random.randint(1, 20)

# print("\nDice 1 is " + str(dice1_number))
# print("Dice 2 is " + str(dice2_number))

# print("Total number is " + str(dice1_number + dice2_number))
