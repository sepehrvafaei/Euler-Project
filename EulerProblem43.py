import itertools
 
p=list(itertools.permutations(list(range(10))))
sigma=0
for d in p:
    if d[0]!=0 and (d[3]%2)==0 and ((d[2]+d[3]+d[4])%3)==0 and\
    (d[5]%5)==0 and ((2*d[4]+3*d[5]+d[6])%7)==0 and\
    ((d[5]-d[6]+d[7])%11)==0 and\
    ((100*d[6]+10*d[7]+d[8])%13)==0 and\
    ((100*d[7]+10*d[8]+d[9])%17)==0:
        num=0
        for i in range(10):
            num+=(10**(9-i))*d[i]
        sigma+=num

print(sigma)
        
        
