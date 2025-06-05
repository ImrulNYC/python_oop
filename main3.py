class User:
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password

    def say_hi_user(self, user):
        print(f"Sending message to {user.username}: HI {user.username}, it is {self.username}")

    def           

              

user1=User("dan", "dan@gmail.com", "1345")

print(user1.email)
user2=User("batman","bat@gmail","233")

user1.say_hi_user(user2)


            