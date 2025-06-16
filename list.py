mylist=[ "banana", "cherry", "apple"]
print(mylist)

item=mylist[2]
print(item)
print(mylist[::-1])

for i in mylist:
    print(i)


if "lemon" in mylist:
    print("yes")
else:
    print("not in")

print(len(mylist))

mylist.append("lemon")
mylist.insert(2,"bluberry")
print(mylist)

mylist.pop()
print(mylist)

mylist.remove(mylist[2])
print(mylist)

newlist=[0]*5
newlist2=[1,2,3,4,5]



new=newlist+newlist2
print(new)

list_org=['banana','apple']

#same list inside the memory
list_cpy=list_org

list_cpy.append("lemon")

print("copy" ,list_cpy)

list_ncopy=list_cpy.copy()

list_ncopy.append('tiger')

print('after copy',list_cpy )

for i in range (len(list_cpy)-1,-1,-1):
    print(list_cpy[i])
