
import random
from Hangman_words import word_list
from Hangman_art import logo
from Hangman_art import stages
print(logo)
life = 6

word_choosed  = random.choice(word_list)
n = len(word_choosed)


your_word = []

for i in range(0,n):
    your_word.append("_")

while not life == 0:
    if not "_" in your_word:
        print("You Won")
        break

    letter = input("Guess the letter ")
    if word_choosed.find(letter) != -1 :
        # x = word_choosed.find(letter)
        for i, char in enumerate(word_choosed):
            if char == letter:
                your_word[i] = letter
        
        print(your_word)
    else:
        life = life - 1
        print(stages[life])

if life == 0:
    print("Game Over")
    print(f"Word was {word_choosed}")
