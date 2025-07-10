#
'''
def mygenerator():
    yield 1
    yield 2
    yield 3

g=mygenerator()

for i in g:
    print(i)

value()


def countdown(num):
    print("Starting")
    while num>0:
        yield num
        num-=1
        


cd=countdown(4)
value=next(cd)


print(next(cd))
'''
import sys

def firstn(n):
    nums=[]
    num=0
    while num <n:
        nums.append(num)
        num +=1
    return nums
    
def firstn_generator(n):
    num=0
    while num<n:
        yield num
        num +=1


print(sum(firstn(10)))
print(sum(firstn_generator(10)))


print(sys.getsizeof(firstn(100000)))
print(sys.getsizeof(firstn_generator(100000)))