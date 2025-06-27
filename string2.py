my_string="Hello world"
print(my_string)

char=my_string[0]
print(char)

substring=my_string[2:5]
print(substring)

substring2=my_string[::2]
substring3=my_string[::-1]

print(substring2)
print(substring3)

for i in my_string:
    print(i)

if 'e' in substring2:
        print("yes e")

elif  'h' in substring2:
    
        print("yes h")
else:
       print("none")


print(my_string.find('o',2))

print(my_string.replace('world', 'Universe'))
print(my_string)

my_string="how, are, you, bro"
mylist=my_string.split(", ")
print(mylist)

new_str='*'.join(mylist)
print(new_str)


new_str2="".join(mylist)
print(new_str2)
print(new_str2.startswith('h'))

newlist=['a']*6
print(newlist)

my_string2= ''

for i in newlist:
       my_string2 +=i
print(my_string2)


##good

my_string3=''.join(newlist)
print(my_string3)
