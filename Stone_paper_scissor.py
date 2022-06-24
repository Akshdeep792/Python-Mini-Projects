import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_list = [rock, paper, scissors]
computer_list = [rock, paper, scissors]
y = input("Enter 0 for rock, 1 for paper, 2 for scissors")
user_choice = user_list[int(y)]
print(f"User's choice\n{user_choice}")
x = random.randint(0,2)

computer_choice = computer_list[x]
print(f"Computer's choice\n{computer_choice}")
if user_choice == paper and computer_choice == rock:
    print("You win")
elif user_choice == rock and computer_choice == scissors:
    print("You Win")
elif user_choice == scissors and computer_choice == paper:
    print("You Win")
else:
    print("You Lost")