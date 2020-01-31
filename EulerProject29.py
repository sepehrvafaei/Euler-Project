from datetime import datetime as dt
def myFunc(n):
    nums=list(range(2,n+1))
    count=0
    distinct=[]
    limit=n**n
    for i in nums:
        for j in nums:
            if i**j not in distinct:
                distinct.append(i**j)

    return len(distinct)

s=dt.now()
print(myFunc(100))
f=dt.now()
print(f-s)
            
            
