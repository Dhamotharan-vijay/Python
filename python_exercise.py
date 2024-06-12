'''sentence ='i am batman and i am 11 and 111 is my lucky number though i like 200'
vowel= 'aeiou'
vowels=[ int(i) for i in sentence.split() if i.isdigit() and  i in '1']
print(sentence.isdigit())
print(max(vowels))'''

'''words=' i am tester and i have a experience of 1.5 year'''

#Pascal Triangle
'''def pascal(n):
    ans=[]
    for i in range(n):
        if i==0:
             prev=[1]
             ans.append(prev)
        else:
            curr=[1]
            j=1
            for j in range(i-1):
                curr.append(prev[j]+prev[j-1])
                j+=1
            curr.append(1)
            ans.append(curr)
            prev=curr
    return ans
print(pascal(5))'''

def pascal(n):
    if n==0:
        return []
    elif n==1:
        return [1]
    else:
        new=[1]
        last=pascal(n-1)
        for i in range(len(last)-1):
            new.append(last[i]+last[i+1])
        new+=[1]
    return new
print(pascal(7))

'''P=lambda h:(lambda x:x+[[x+y for x,y in zip(x[-1]+[0],[0]+x[-1])]])(P(h-1))if h>1 else[[1]]
print(P(5))'''
                
    
