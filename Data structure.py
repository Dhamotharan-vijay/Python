#List

'''list=['cars','cycles','bike',[1,2,3,4]]
print(list[-1])
print(len(list))'''

'''list2=list(range(10,20))
print(list2) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19] list keyword is imp.

list2.append(110)
print(list2) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 110]

list2[2]=23
print(list2)#[10, 11, 23, 13, 14, 15, 16, 17, 18, 19, 110]

for i in range(20,30):
    list2.append(i)
    
print(list2)
list2.insert(2,12)#position,values
print(list2)

li=[1,2,3]
le=[4,5,6]
li.extend(le)
print(li)#[1, 2, 3, 4, 5, 6]

list2.remove(23)#value 
print(list2)
li.pop(0)
print(li)#index [2, 3, 4, 5, 6]
li.reverse()
print(li)'''

#list comprehension

odd=[i**2 for i in range(2,8) if i%2!=0]
print(odd)#[9, 25, 49]

arr=[1,0,0,1,0]
#to extract 0 & 1 and print in sequentially
res=[i for i in arr if i==0]+([i for i in arr if i==1])
print(res)






