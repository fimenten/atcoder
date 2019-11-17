N=int(input())
S=list(input())
ret=0
for i in range(N):
    if i==0:
        p=S[i]
        ret=ret+1
    else:
        n=S[i]
        if n==p:
            continue
        else:
            p=n
            ret=ret+1
print(ret)

