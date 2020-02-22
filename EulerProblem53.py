L1=[1,1]
L2=[1]
count=0
for k in range(99):
    for i in range(1,len(L1)):
        L2.append(L1[i-1]+L1[i])
    L2.append(1)
    for j in L2:
        if j>10**6:
            count+=1
    L1=L2
    L2=[1]
        
print(count)
