N=int(input())
L_list=[int(thing) for thing in input().split()]
L_list.sort(reverse=True)

ret=0

s_list=[]

for i in range(N-2):
    n=L_list[i]
    diff=0
    for j in range(i+1,N-1):
        k=L_list[j]
        m=n-k
        s=0
        for h in range(j+1,N):
            if L_list[h]>m:
                s=s+1
            else:
                break
        s_list.append(s)
        if s==0:
            break
        else:diff=diff+s
    ret=ret+diff
print(ret)
print(s_list)