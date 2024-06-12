#lambda expression
'''s=lambda x: x**2
print(s(9))
print((lambda x: x**2)(9))'''
#lambda are anonymous function  since we need not store it in a variable

#=========================================================

def funct():
    x=5
    if x>5:
        print(1)
    else:
        print(2)
funct()
s=lambda x:print(1) if x>5 else print(2)
s(2)
#lamba dont take elif condition

#=========================================================

from functools import reduce
'''-reduce(func,iterator)
-need not convert into list like map or filter
'''
from functools import reduce as rd
a = range(1, 11)
res = rd(lambda x, y: x + y, a)
print(res)
#55
print(list(a))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#========================================================

'''zip can take n number of args'''

#=========================================================

'''args will be passed as tuple
u can access the elements in args using loop
*args cannot be used before arguments
but only exception of default arguments'''

'''def add_func(a,*args,b= 2):
    sum = a+b
    for i in args:
        sum+=i
    return sum

add_func(1,2,3,4) '''

'''def add_func(a,*args,b):
    sum = a+b
    for i in args:
        sum+=i
    return sum

add_func(1,2,3,4) '''

#=========================================================
'''kwargs will be passed as dict '''