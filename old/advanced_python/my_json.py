#encoding
import json #javascript object notation

"""person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent = 4) #dumps -> dump string
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent = 4) #dump -> dumping into json
    print("file created.")

a = json.loads(personJSON) #loads -> load string
print(a)

with open('person.json', 'r') as file:
    b = json.load(file) #load -> load a json file into dict.
    print(b)"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Salah', 31)

def encode_user(o):
    if isinstance(o, User):
        return {'name' : o.name, 'age' : o.age, o.__class__.__name__ : True}
    else:
        raise TypeError

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

from json import JSONEncoder
class UserEncoder(JSONEncoder) :

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True }
        return JSONEncoder.default(self, o)

userJSON = UserEncoder().encode(user)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct ['name'], age=dct ['age' ])
    return dct

user = json. loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)