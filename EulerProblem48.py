def func(n):
    sigma=0
    for i in range(1,n):
        sigma+=i**i

    return sigma

print(func(1000))
    
