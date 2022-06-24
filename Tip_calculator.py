print("Welcome to tip calculator.")

bill = input("What was the bill? Rs.")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")

total_members = input("How many people to split bill?")

total_tip = float(bill) * float(tip) / 100
total_bill = float(bill) + total_tip

each_person = float(total_bill) / float(total_members)
x = round(each_person, 2)
print(f"Each person should pay: Rs {x}")