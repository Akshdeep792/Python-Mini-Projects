from art import logo
import os
print(logo)

bid_info = {}


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def declare_winner():
    winner_bid = 0
    winner_name = ""
    print(bid_info)
    for key in bid_info:
        if bid_info[key] > winner_bid:
            winner_name = key
            winner_bid = bid_info[key] 
    
    print(f"{winner_name} wins the auction with the highest bid of {winner_bid}")

def enter_info():
    name = input("Enter Your Name: ")
    bid_price = input("Enter your bid price $")

    bid_info[name] = int(bid_price)
    any_other = input("Any One wants to bid? ")

    if any_other == "yes":
        clearConsole()
        enter_info()
    elif any_other == "no":
        declare_winner()

enter_info()


