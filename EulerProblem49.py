import math
import itertools
arr=[True for i in range(1,10000)]
arr[0]=False
arr[1]=False
for i in range(2,100):
    if arr[i]==True:
        for j in range(i**i,9999,i):
            arr[j]=False

dic={}
for i in range(1000,9999):
    if arr[i]==True:
        dic[i]=''.join(sorted(str(i)))

d = {n:[k for k in dic.keys() if dic[k] == n] for n in set(dic.values())}

for i in d.values():
    if len(i)==3:
        if abs(i[1]-i[0])==3330 and abs(i[2]-i[1])==3330:
            print(i)
    elif len(i)>3:
        for j in itertools.combinations(i,3):
            if abs(j[1]-j[0])==3330 and abs(j[2]-j[1])==3330:
                print(j)




    
    
        
