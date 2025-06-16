import sys
mylist=[0,1,2.0,"hello",True]
mytuple=(0,1,2.0,"hello",True)
print(sys.getsizeof(mylist),"bytes")
print(sys.getsizeof(mytuple)," bytes")

import timeit
print(timeit.timeit(stmt="[1,2,3,4,4,4]",number=10000000))
print(timeit.timeit(stmt="(1,2,3,4,4,4)",number=10000000))


