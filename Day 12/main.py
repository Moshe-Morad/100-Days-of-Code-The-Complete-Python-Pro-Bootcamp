import math


def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")


def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


def add_new_country(f_country, f_visits, f_list_of_cities):
    travel_log.append({"country": f_country, "visits": f_visits, "cities": f_list_of_cities})


# paint_calc(2, 4, 5)
# prime_checker(73)
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

