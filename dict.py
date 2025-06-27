mydict={
"name": "Max", "age": 28, "city":"New York"
}

print(mydict)
print(mydict.values())

print(mydict.keys())

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("error")



for value in mydict.values():
    print(value)

for key,value in mydict.items():
    print(f"{key} , {value}")


