from datetime import datetime as dt
from itertools import permutations
nums=list(range(1,10))
p=[]
count=0
d_4=0
for i in list(permutations(nums, 2)):
        d_2=10*i[0]+i[1]
        for j in list(permutations([x for x in nums if x not in i],3)):
                d_3=100*j[0]+10*j[1]+j[2]
                d_4=d_2 * d_3
                d4l=[int(x) for x in list(str(d_4))]
                d4l.sort()
                if len(d4l)==4:
                        if d4l == sorted([x for x in nums if (x not in i and x not in j)]):
                                if d_4 not in p:
                                        p.append(d_4)
                                        


d_4_p=0
for i in list(permutations(nums,4)):
        d_4=1000*i[0]+100*i[1]+10*i[2]+i[3]
        for j in [x for x in nums if x not in i]:
                d_4_p=d_4 * j
                d4pl=[int(x) for x in list(str(d_4_p))]
                d4pl.sort()
                if len(d4pl)==4:
                        if d4pl == sorted([x for x in nums if (x != j and x not in i)]):
                                if d_4_p not in p:
                                        p.append(d_4_p)



s=dt.now()
print(p)
sigma=0
for i in p:
        sigma+=i
print(sigma)
f=dt.now()
print(f-s)

                                
                        
                          
