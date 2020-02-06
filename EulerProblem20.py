product=1
for i in range(1,101):
    product*=i

string=str(product)
sigma=0
for i in range(len(string)):
    sigma+=int(string[i])

print(sigma)
