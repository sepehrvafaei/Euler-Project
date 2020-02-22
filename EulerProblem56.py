maximum=0
sigma=0
for a in range(1,101):
    for b in range(1,101):
        sigma=0
        n=str(a**b)
        for i in range(len(n)):
            sigma+=int(n[i])
        if sigma>maximum:
            maximum=sigma

print(maximum)
            
