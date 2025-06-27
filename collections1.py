#counter

from collections import Counter

a='aaaabbbccc'
mycounter=Counter(a)
print(mycounter)
print(mycounter.values())
print(mycounter.keys())

print(mycounter.most_common(2)[0][0])
print(list(mycounter.elements()))

from collections import namedtuple
Point=namedtuple('Point','x,y')
pt=Point(10,20)
print(pt)

from collections import OrderedDict

ordered=OrderedDict()

ordered['a']=5
ordered['b']=3
ordered['d']=3
ordered['a']=6
print(ordered)

from collections import defaultdict

d=defaultdict(int)

d['a']=1
d['b']=-2

print(d.keys(),d.values())

from collections import deque

ninja=deque()
ninja.append(1)
ninja.append(4)
ninja.appendleft(5)
ninja.append(6)
ninja.appendleft(15)
print(ninja)
ninja.popleft()
print(ninja)