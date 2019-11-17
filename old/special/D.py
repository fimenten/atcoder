import bisect
N,K=[int(thing) for thing in input().split(" ")]
ll=[]
pool=list(range(K,K+2*N))
for i in range(0,N):
    c=K+3*N-1-i
    b=pool[-1]
    aa=c-b+1
    index=bisect.bisect_left(pool,aa)-1
    if index==len(pool):
        print(-1)
        exit()
    a=pool.pop(index)
    if a==b:
        print(-1)
        exit()

    ll=[[a,b,c]]+ll

for l in ll:
    print(l)
    print(" ".join([str(thing) for thing in l]))

