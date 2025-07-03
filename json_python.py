import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJson=json.dumps(person,indent=4,sort_keys=True)
print(personJson)

with open ('person.json', 'w') as file:
    json.dump(person,file,indent=4)


with open ('person.json' , 'r') as file:
    person2=json.load(file)

print(f"person2 {person2}")