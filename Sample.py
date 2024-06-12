'''class Sample:
    def __init__(self,age):
        self.age=age
h=Sample(10)
print(h.age)'''
#==========================
# local non local global variable
'''def name_fun():
    def local_function():
      name='Dhamo'
    def non_local():
      nonlocal name
      name='Tharan'
    def global_fun():
         #keyword
        global name
        name = 'DA'
    name='bb'
    print(name)
    local_function()
    print(name)
    non_local()
    print(name)
    global_fun()
    print(name)
name_fun()
print(name)'''
#==========================
'''def sort_list(A):
  count=[0,0,0]
  for num in A:
    count[num]+=1
  print(count)   #[5, 5, 2]
  index=0
  for i,value in enumerate(count):
    while value!=0:
      A[index]=i
      index+=1
      value-=1
  return A'''
#==========================
'''def sort_list(A):
  ln=len(A)
  l=0
  m=0
  h=ln-1
  while m<=h:
    if(A[m]==0):
      A[l],A[m]=A[m],A[l]
      l+=1
      m+=1
    elif A[m]==1:
      m+=1
    else:
      A[h],A[m]=A[m],A[h]
      h-=1
      m+=1
  return A
# this algo has three pointers l,m,h if i is equal to value move the pointer by swapping the values

A=([1, 2, 1, 2, 1, 2])
print(sort_list(A))'''
#This code fails for certain TC better to follow the previous approach
#==========================

#array row -wise sum
'''A=[[1,2,3,4],[5,6,7,8],[9,2,3,4]]
def two_d(A):
  len_row=len(A)
  len_col=len(A[0]) # getting no of col from row
  ans=[]
  for i in range(len_row):
    sum=0
    for j in range(len_col):
      sum+=A[i][j]
    ans.append(sum)
  return ans 
print(two_d(A))
'''
#array col -wise sum
'''def two_d(A):
  len_row=len(A)
  len_col=len(A[0]) # getting no of col from row
  ans=[]
  for i in range(len_col):
    sum=0
    for j in range(len_row):
      sum+=A[j][i]
    ans.append(sum)
  return ans 
print(two_d(A))
#==========================
A=[[1,2,3,4],[5,6,7,8],[9,2,3,4]]
ans=[]
for i in range(0,len(A[0])):
  temp = []
            # Iterating over the rows
  for j in range(0,len(A)):
    temp.append(A[j][i])
  ans.append(temp)'''


    

