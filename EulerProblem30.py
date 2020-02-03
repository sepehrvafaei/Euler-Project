wanted=[]
for i in range(1,10):
    j=10-i
    s=100*i+10*j-i**5-j**5
    for k in range(0,10):
        if s==(k**5-k):
            wanted.append(100*i+10*j+k)

for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            if (a+b+c)%10 == 0:
                s=(1000*a+100*b+10*c)-(a**5+b**5+c**5)
                for d in range(0,10):
                    if s == (d**5-d):
                        wanted.append(1000*a+100*b+10*c+d)


for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                if (a+b+c+d)%10 == 0:
                    s=(10000*a+1000*b+100*c+10*d)-(a**5+b**5+c**5+d**5)
                    for e in range(0,10):
                        if s == (e**5-e):
                            wanted.append(10000*a+1000*b+100*c+10*d+e)


for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    if (a+b+c+d+e)%10 == 0:
                        s=(100000*a+10000*b+1000*c+100*d+10*e)-(a**5+b**5+c**5+d**5+e**5)
                        for f in range(0,10):
                            if s == (f**5-f):
                                wanted.append(100000*a+10000*b+1000*c+100*d+10*e+f)
                            


print(wanted)

total=0
for i in wanted:
    total+= i

print(total)
