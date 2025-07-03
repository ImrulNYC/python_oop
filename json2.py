import json

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user=User('Max',27)


def encode_user(o):
    if isinstance(o,User):
        return {'name':o.name, 'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError("Object is not the json ")


from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o) :
        if isinstance(o,User):
            return {'name': o.name, 'age':o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
    



userJSON=json.dumps(user,cls=UserEncoder)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct



user2=json.loads(userJSON,object_hook=decode_user)
print(f"Decode, {user2}")
