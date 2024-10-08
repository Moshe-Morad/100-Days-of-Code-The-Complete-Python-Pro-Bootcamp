from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_counter = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()


is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_counter.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_machine.is_resource_sufficient(drink) and money_counter.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)


