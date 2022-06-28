import random
print("Welcome to Number Guessing Name!")
print("I am thinking of number between 1 and 100")

def next_level(attempts, num):
    while not attempts == 0:

        print(f"You have {attempts} remaining to guess the number")
        your_num = input("Make a guess. ")

        if int(your_num) == num:
            print("You Win! Your guess was correct")
            return
        elif int(your_num) > num and int(your_num) < num + 10 :
            print("High! ")
            attempts = attempts - 1;
           
        elif int(your_num) < num and int(your_num) > num - 10:
            print("Low! ")
            attempts = attempts - 1;
        elif int(your_num) > num + 10:
            print("Too High! ")
        elif int(your_num) < num -10:
            print("Too Low!")
    
    print("Your attempts are over!")
    print("Game Over")
    return

def game_start(diff,x):
    if diff == "easy":
        next_level(10,x)
    elif diff == 'hard':
        next_level(5,x)

x = random.randint(0,101);
print(x)
diff = input("Choose difficulty. Type easy or hard. ")

game_start(diff, x)