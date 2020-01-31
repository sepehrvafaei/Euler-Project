def isPalindrome(n):
    s= str(n)
    return s ==s[::-1]

def myFunc():
    largest=0
    for i in range(100,1000):
        for j in range(100,1000):
            if isPalindrome(i*j)and i*j>largest:
                largest=i*j
    return largest

print(myFunc())
