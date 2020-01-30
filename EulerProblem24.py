import math
def myFunc(nums,order):
    n=len(nums)
    p=[]
    rest=nums
    m=order
    while m>1:
        temp=m/math.factorial(n-1)
        if temp==int(temp):
            index=int(temp-1)
        else:
            index=int(temp)
        p.append(rest[index])
        rest.remove(rest[index])
        m=m-index*math.factorial(n-1)
        n-=1
    p.extend(rest)
    return p

nums=list(range(10))
print(myFunc(nums,1000000))
