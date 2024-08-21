import menu_data
from menu_data import resources, profit


def parsed_data():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def is_resources_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough water.")
            is_enough = False
            return is_enough
    return is_enough


def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please enter coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return round(total, 2)


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def format_machine():
    if resources["water"] <= 300 or resources["milk"] <= 200 or resources["coffee"] <= 100:
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
        print("Turning off 😴")
    elif choice == "report":
        parsed_data()
    elif choice == "format":
        format_machine()
    else:
        drink = menu_data.MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            print(f"You entered ${payment}")
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

