import random
from itertools import count

# name = "Angela"
# # formula = new_list = [new_item for item in list]
# letters_list = [letter for letter in name]
# print(letters_list)


# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# all_caps = [name.upper() for name in names if len(name) > 5]
# print(all_caps)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [eval(n) for n in list_of_strings]
# result = [number for number in numbers if number % 2 == 0]
# print(result)

# with open("file1.txt") as file1:
#     file1_read = [int(n) for n in file1.read().split()]
#
# with open("file2.txt") as file2:
#     file2_read = [int(n) for n in file2.read().split()]
#
# result = [number for number in file1_read if number in file2_read]
#
# print(result)


#Dictionary Comprehension
# formula:  new_dict = {new_key:new_value for item in list}, new_dict = {new_key:new_value for (key,value in dict.items()},
# new_dict = {new_key:new_value for (key,value in dict.items() if test}

# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
#
# passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

# Coding Exercise 1
"""You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.   
Try Googling to find out how to convert a sentence into a list of words.  *
*Do NOT** Create a dictionary directly.
Try to use Dictionary Comprehension instead of a Loop. 

To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.↧"""
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word: len(word) for word in sentence.split()}
# print(result)

# Coding Exercise 2
"""You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 

To convert temp_c into temp_f use this formula: 
(temp_c * 9/5) + 32 = temp_f

Celsius to Fahrenheit chart


**Do NOT** Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.↧"""

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# print(weather_c)
#
# weather_f = {day: (temp_c * 9/5) + 32 for day, temp_c in weather_c.items()}
#
# print(weather_f)
