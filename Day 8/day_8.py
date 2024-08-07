# -*- coding: utf-8 -*-
"""Day 8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tqxaML4nubaH0dTFZs-ATya0ibr8rbKx
"""

# Function without inputs
def greet():
  print("Hello")
  print("There")
  print("What's Up?")

greet()

# Function that allows for inputs
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
  print(f"{name}, Isn't the weather nice?")

greet_with_name("Moshe")

def life_in_weeks(age):
    years = 90 - age
    weeks = years * 52

    print(f"You have {weeks} weeks left")

life_in_weeks(20)

# Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
  print(f"{name}, Isn't the weather nice in {location}?")

# greet_with("Moshe", "Israel")
greet_with(location = "Israel", name = "Moshe")

# Caesar Cipher

logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.



#TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted
# Example with the word "hello"
def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text: #moving letter by letter in the word that the user give
    position = alphabet.index(letter) #search the number of the letter in the list 'h' = 7
    new_position = position + shift_amount #increse the number in the list by the amount the user give 7 + shift_amount
    new_position %= len(alphabet)
    new_letter = alphabet[new_position] #extracting the new letter from the list. the_list[7 + shift_amount]
    cipher_text += new_letter
  print(f"The encoded text is '{cipher_text}'")

def decrypt(plain_text, shift_amount):
  decrypt_cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    new_position %= len(alphabet)
    new_letter = alphabet[new_position]
    decrypt_cipher_text += new_letter
  print(f"The decoded text is '{decrypt_cipher_text}'")


def caesar(plain_text, shift_amount, encode_or_decode):
  output_text = ""
  if encode_or_decode == "decode":
        shift_amount *= -1
  for letter in plain_text:
    position = alphabet.index(letter)
    if letter not in alphabet:
      output_text += letter
    else:
      new_position = position + shift_amount
      new_position %= len(alphabet)
      new_letter = alphabet[new_position]
      output_text += new_letter
  print(f"The {encode_or_decode}d text is '{output_text}'")

processed = True
print(logo)
while processed:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(plain_text = text, shift_amount = shift, encode_or_decode = direction)
  answer = input("Would you like to processed?\n").lower()
  if answer == "no":
    processed = False

