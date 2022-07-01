from telnetlib import X3PAD
from tkinter import Menu


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 20,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money" : 0
}

def making_coffee(x):
        if MENU[x]["ingredients"]["water"] <= resources["water"] and MENU[x]["ingredients"]["milk"] <= resources["milk"] and MENU[x]["ingredients"]["coffee"] <= resources["coffee"]:
            print("Please insert coins")
            quarters = input("How many quarters? ")
            dime = input("How many dimes? ")
            nickles = input("How many nickels? ")
            pennies = input("How many pennies? ")
            t_cost = total_cost(int(quarters), int(dime), int(nickles), int(pennies))
            if t_cost >= MENU[x]["cost"]:
                resources["water"] = resources["water"] - MENU[x]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[x]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[x]["ingredients"]["coffee"]
                resources["Money"] = resources["Money"] + t_cost
                print(f"Here is your {x} ☕ Enjoy! ")
            else:
                print("Not Enough Money. Money Refunded!")
        elif MENU[x]["ingredients"]["water"] > resources["water"]:
            print("Sorry There is Not Enough Water")
        elif MENU[x]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry There is Not Enough Milk")
        elif MENU[x]["ingredients"]["coffee"]  > resources["coffee"]:
            print("Sorry There is Not Enough coffee")

def total_cost(q, d, n, p):

    q = q * 0.25
    d = d * 0.10
    n = n * 0.05
    p = p * 0.01
    
    return q+d+n+p

def show_report(resources):
    print(resources)

def make_coffee(resources, MENU):
    x = input("What would you like? (espresso/latte/cappucino)")

    if x == "report":
        show_report(resources)     
    else:
        making_coffee(x)


    make_coffee(resources, MENU)

    
make_coffee(resources, MENU)