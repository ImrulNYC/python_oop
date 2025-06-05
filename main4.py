
from datetime import datetime
class User:
       ## mangled , can not accessed outusde of class, 
    # 
    ## protected _  , private __
    def __init__(self,username,email,password):
        self.username=username
        self._email=email
        self.password=password

    @property
    def email(self):

        print(f" email was accesed at {datetime.now()}")
        return self._email
    
    @email.setter
    def email(slef,new_email):
        if "@" in new_email:
            self._email=new_email
    



    ##def get_email(self):
        ##return self.__email

    def get_email(self):
        print(f"email was accessed at {datetime.now()}")
        return self._email
    
    def set_email(self,new_email):
        if "@" in  new_email:
         self._email=new_email
    

    
    def clean_email(self):
        return self.__email.lower().strip()



user1=User("dan", "Dan@gmail.com", "1345")


print(user1.get_email())
user1.set_email("abc@gmail.com")
print(user1.get_email())

print(user1.email)
