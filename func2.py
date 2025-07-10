def foo(a_list):
    a_list.append(4)



mylist=[1,2,3]
foo(mylist)
print(mylist)


def foo2(a_list2):
    global mylist2
    a_list2=[10,20,30]

    a_list2=mylist2
    

    a_list2.append(4)
    a_list2[0]= -100
    print(a_list2)


mylist2=[1,2,3]
foo2(mylist2)
print(mylist2)

def foo3(a_list3):
    #a_list=a_list+[100,200,300]
    print("inside of foo3",a_list3)
    a_list3=a_list3+[100,200,300]
    print("not using addd method",a_list3)

a_list3=[1,2,3]
foo3(a_list3)
print(a_list3)
