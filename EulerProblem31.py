def myFunc(n):
    count=0
    for h in range(0,2):

        for g in range(0,int((n-200*h)/100)+1):

            for f in range(0,int((n-200*h-100*g)/50)+1):

                for e in range(0,int((n-200*h-100*g-50*f)/20)+1):

                    for d in range(0,int((n-200*h-100*g-50*f-20*e)/10)+1):

                        for c in range(0,int((n-200*h-100*g-50*f-20*e-10*d)/5)+1):

                            for b in range(0,int((n-200*h-100*g-50*f-20*e-10*d-5*c)/2)+1):

                                for a in range(0,int((n-200*h-100*g-50*f-20*e-10*d-5*c-2*b)/1)+1):

                                    if(200*h+100*g+50*f+20*e+10*d+5*c+2*b+a)==n:
                                        count+=1

    return count

print(myFunc(200))
