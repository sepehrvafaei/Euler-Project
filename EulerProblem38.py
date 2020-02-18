largest=0
for i in range(1,9999):
    s=''
    n=1
    while len(s)<9:
        s=s+str(i*n)
        n+=1
    if len(s)<=9:
        if sorted(s)==sorted('123456789'):
            if int(s)>largest:
                largest=int(s)
            

print(largest)
