def perfect_number(x):
    div= [i for i in range(1,x) if x % i==0]
    return sum(div)
    