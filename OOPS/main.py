class User:
    

    def  __init__(self, name):
        self.userName = name
        self.followers = 0
        self.following = 0
        print("User object created")
    def increase_follower(self, user):
        user.following +=1
        self.followers += 1
    

user1= User("Akshdeep Singh")
user2 = User("Raman")
print(user1.userName)
print(user1.followers)
user1.increase_follower(user2)
print(user1.followers)



