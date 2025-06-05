

class User:
    user_count=0

    def __init__(self,username,email):
        self.username=username
        self.email=email
        User.user_count +=1

    def display_user(self):
        print(f"Username: {self.username}, email ;{self.email}")



user1=User("abc", "abc@tgmaul.ocm")


print(user1.user_count)
print(User.user_count)
