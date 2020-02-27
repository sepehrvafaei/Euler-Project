import math
from datetime import datetime as dt
start=dt.now()
def Func(i):
    sigma=0
    temp=math.sqrt(i)
    for j in range(1,int(temp)+1):
        if (i%j)==0:
            sigma+=(j+i//j)
    if int(temp)==temp:
        sigma-=temp
    return int(sigma-i)

dic={}
for j in range(2,10**6+1):
    temp=Func(j)
    if temp<=10**6:
        dic[j]=temp
largest=0
wanted=0
for i in dic.keys():
    try:
        count=0
        j=dic[i]
        keep=[j]
        while j!=i:
            if j==1:
                count=0
                break
            j=dic[j]
            if j not in keep:
                keep.append(j)
                count+=1
            else:
                count=0
                break
        if count>largest:
            largest=count
            wanted=i
    except KeyError:
        continue
        

print(wanted)
finish=dt.now()
print(finish-start)
