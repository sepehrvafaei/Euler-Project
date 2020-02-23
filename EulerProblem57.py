a=1
b=1
c=0
for i in range(1000):
    t=a
    a=a+2*b
    b=t+b
    if len(str(a))>len(str(b)):
        c+=1

print(c)
