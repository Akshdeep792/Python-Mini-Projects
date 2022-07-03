# from turtle import Turtle, Screen

# timmy = Turtle()

# # print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(1000)
# print(timmy.position())

# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Name", ["Charizard", "Lucario", "Sceptile", "Zeraora"])
# table.add_column("Type", ["Fire/dragon", "Steel/Fighting", "Grass", "Electric"])

# table.align = "l"

# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_On = True

while is_On:

    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_On = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
