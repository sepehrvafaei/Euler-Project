from itertools import permutations,combinations

arr=list(combinations(list(range(10)),4))
l=[]
wanted=[]
for i in arr:
    l=list(permutations(list(i)))
    num=0
    for j in l:
        if j[0]!=0:
            num=j[0]*10**3+j[1]*10**2+j[2]*10+j[3]
            if isPrime(num):
                wanted.append(num)
    
    
