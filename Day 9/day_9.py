# -*- coding: utf-8 -*-
"""Day 9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kzWI9Skr6tm7ZcJ4rF0PeywaFToAKIwO
"""

# Dictionaries
#{Key: Value}
#{"Bug": "An error we've created an actual  dictionary using Python code"}
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary["Bug"])

# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# empty_dictionary = {}

# programming_dictionary = {}
# print(programming_dictionary)

# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades.

# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.

# The final version of the student_grades dictionary will be checked.

# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary.

# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# print(student_scores)
# student_grades = {

# }
# for key in student_scores:
#     if student_scores[key] > 91 and student_scores[key] < 100:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] > 81 and student_scores[key] < 90:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] > 71 and student_scores[key] < 80:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
# print(student_grades)

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "lille", "Dijon"],
#     "Germany": ["stuttgart", "Berlin"],
# }
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
print(travel_log["Germany"]['cities_visited'][2])

def clear():
  print("\n" * 50)

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


print(logo)
while bidding_finished != True:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()