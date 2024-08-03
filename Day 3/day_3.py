# -*- coding: utf-8 -*-
"""Day 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ri5WWr1LpZx7Z29F7Fxj74zs-YEQMQSE
"""

# Operator    Meaning
#     >       Grather than
#     <       Less than
#    >=       Grather than or equal to
#    <=       less than or equal to
#    ==       Equal to
#    !=       Not equal to
#     =       Assign variable

# if condition:
#   do this
# else:
#   do this

# if condition1:
#   do A
# elif condition2:
#   do B
# else:
#   do this

water_level = 50
if water_level > 80:
  print("Drain water")
else:
  print("Continue")

#rollercoaster
print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

number = int(input())

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# Nested if / else
# if condition:
#   if another condition:
#     do this
#   else:
#     do this
# else:
#   do this

#rollercoaster ticket
print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age >= 18:
    print("You need to buy the $12 ticket")
  else:
    print("There you go!, your $7 ticket")
else:
  print("Sorry, you have to grow taller before you can ride.")

#rollercoaster ticket
print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("your $5 ticket")
  elif age <= 18:
    print("your $7 ticket")
  else:
    print("your $12 ticket")
else:
  print("Sorry, you have to grow taller before you can ride.")

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#leap year

year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

#rollercoaster with photo

print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print(f"Child tickets are ${bill}.")
  elif age <= 18:
    bill = 7
    print(f"youth tickets are ${bill}.")
  else:
    bill = 12
    print(f"Adult tickets $${bill}.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    #Add $3 to their bill
    bill += 3

  print(f"Your final bill is {bill}.")

else:
  print("Sorry, you have to grow taller before you can ride.")

#My Way
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N ") # Do you want extra cheese? Y or N
bill = 0

if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
if size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
if size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")

#Course Way
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N ") # Do you want extra cheese? Y or N
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

# Logical Operators
# option1 and option2
# option1 or option2
# not option1

#rollercoaster with photo midlife crisis

print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print(f"Child tickets are ${bill}.")
  elif age <= 18:
    bill = 7
    print(f"youth tickets are ${bill}.")
  elif age >= 45 and age <= 55:
    print(f"Everything is going to be ok. Have a free ride on us! tickets are ${bill}.")
  else:
    bill = 12
    print(f"Adult tickets $${bill}.")


  wants_photo = input("Do you want a photo taken? Y or N. ").lower()

  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is {bill}.")

else:
  print("Sorry, you have to grow taller before you can ride.")

#Love Calculator

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road_choice = input("You're"' at a cross road. Where do you want to go?\nType "left" or "right" ').lower()
if road_choice == "left":
  boat_or_swim = input("You've come to a lake. There is an island in the middle of the lake."'\nType "wait" to wait for the boat. Type "swim" to swim across ').lower()
  if boat_or_swim == "wait":
    door_choose = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which color do you choose? ").lower()
    if door_choose == "red":
      print("Burned by fire. Game Over")
    elif door_choose == "yellow":
      print("You found the treasure! You Win!")
    elif door_choose == "blue":
      print("Eaten by beasts. Game Over")
    else:
      print("Game Over")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")