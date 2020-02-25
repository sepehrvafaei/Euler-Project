import math

file=open('p099_base_exp.txt','r')
largest=0
count=0
wanted=0
for line in file:
    count+=1
    arr=line.strip().split(',')
    temp=int(arr[1])*math.log10(int(arr[0]))
    if temp>largest:
        largest=temp
        wanted=count

print(wanted)


        
    
