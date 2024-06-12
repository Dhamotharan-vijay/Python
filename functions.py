'''All variable inside the function is local variable 
and outside that is global variable'''
#def name(arg)

'''def p_rint():
    print('this is a function')
p_rint()'''

'''def perfect_number(a):
    count=0
    for i in range(1,int(a**(1/2))+1):
        if(a%i==0):
            if(i==a/i):
                count=count+1
                print("huweuwu")
            else:
                count=count+2
    return count
print(perfect_number(100))
'''
#========================================
#*args can be used to pass multiple parameters.
'''
def ag(*args):
    sum=0
    for arg in args:
        sum = sum+arg
    return sum
print(ag(1,2,3,4))
'''
#====================================
#**kwargs is used to pass keyword args.
'''def fun(**kwargs):
    for value in kwargs.items():
        print(value)
        
fun(one="print one",second="print two")'''
#========================================

#Lambda function
def  func(x):
    if (x%2==0):
        return("even")
    else:
        return("odd")

#(func(3))
#writing the same function using Lambda

function =lambda x : "even"if x%2==0 else "odd"
#print(function(11))

#if u give print insted of return in the statement the function it will display
'''output : odd
even
odd
'''


'''print(map(func,[1,2,3]))   #<map object at 0x000001B35BAB5F00>
print(list(map(func,[1,2,3])))   #['odd', 'even', 'odd']
print(set(map(func,[1,2,3])))  #{'even', 'odd'} no duplicates
print(tuple(map(func,[1,2,3]))) #('odd', 'even', 'odd')'''

#tha same logic with lambda function
'''print(list(map(function,[1,2,3,4,5]))) #['odd', 'even', 'odd', 'even', 'odd']
print(set(map(function,[1,2,3,4,5])))  #{'odd', 'even'}'''

numbers =[2,4,5,2,1,4,993,1090]
def oddEven(x):
    if x%2==0:
        return True
    else:
        return False
#filter is used only for boolean condition
print(filter(oddEven,numbers)) #<filter object at 0x0000025FA94A5BD0>
print(list(filter(oddEven,numbers)))#[2, 4, 2, 4, 1090]

#zip is used to map two values while map is used to map mmultiple values to function
names=['dhamo','tharan','dhanush']
jerseyNo=[7,22,11]
print(list(zip(names,jerseyNo))) #[('dhamo', 7), ('tharan', 22), ('dhanush', 11)]

for names,jerseyNo in list(zip(names,jerseyNo)):
    print(names ,'jersey number', jerseyNo)
'''dhamo jersey number 7
tharan jersey number 22
dhanush jersey number 11'''


def oddeven(x):
    if x%2==0:
         return True
    else:
        return False
    
print(tuple(map(oddeven,[22,3,5,6,7,8])))

l=['dhamo','revinn','ajth','arjun']
print(list(map(set,l)))

    




