my_list=[12,24,31]

print(list(map(lambda item : item*2, my_list)))

print(list(filter(lambda item : item %2 ==0,my_list)))


a=[(0,2), (3,2), (4,3), (8,3), (0,9)]

a.sort(key=lambda x : x[1])


a.sort(key=lambda x:x[1] )
print(a)

#based on 
