def primeTillN(n):
    for i in range(2,n+1):
        isPrime=1
        for j in range(2,int(n**0.5)+1):
             if i%j==0:
                 isPrime=0
                 break
        if isPrime==1:
             print(i,end=' ')
primeTillN(19)

