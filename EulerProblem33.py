for a in range(1,8):
    for c in range(a+1,10):
        for b in range(c+1,10):
            if (10*a+b)/(10*b+c) == a/c :
                print((10*a+b),'divided by',(10*b+c) )
