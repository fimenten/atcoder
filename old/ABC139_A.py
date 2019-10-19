S=list(input())
T=list(input())
ret=0
for s,t in zip(S,T):
    if s==t:
        ret=ret+1
print(ret)