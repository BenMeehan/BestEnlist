# Day 16

# 1.
x=lambda a,b:a*b 
print(x(2,3))

# 2. 
from functools import reduce
f = lambda y: reduce(lambda x, _: x + [x[-1] + x[-2]], range(y - 2), [0, 1])
print(f(8))

# 3.
l=lambda li,n:[i*n for i in li]
print(l([1,2,3],3))

# 4.
nine=lambda li:[i for i in li if i%9==0]
print(nine([1,2,3,10,11,18]))

# 5.
even=lambda li:len([i for i in li if i%2==0])
print(even([1,2,3,4]))