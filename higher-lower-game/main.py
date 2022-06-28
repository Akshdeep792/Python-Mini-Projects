import random
from game_data import data
from art import logo, vs

print(logo)

a = random.choice(data)
b = random.choice(data)
count = 0;
# print(a["name"])
# print(a["follower_count"])
def compare(a, b, count):
    name = a["name"]
    follower_count = a["follower_count"]
    description = a["description"]
    country = a["country"]
    print(f"Compare A: {name}, {description}, {country}")
    print(vs)

    name_b = b["name"]
    follower_count_b = b["follower_count"]
    description_b = b["description"]
    country_b = b["country"]
    print(f"Against B: {name_b}, {description_b}, {country_b}")

    res = input("Who has more followers? A or B ")

    if follower_count > follower_count_b and res == "B":
        print(f"Your score is: {count}")
    elif follower_count_b > follower_count and res == "A":
        print(f"Your score is: {count}")
    else:
        count+=1
        x = random.choice(data)
        if res == "A":
            compare(a,x, count)
        else:
            compare(b,x,count)
        

compare(a,b, count);