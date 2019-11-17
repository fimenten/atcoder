N=int(input())
L_list=[int(thing) for thing in input().split()]
L_list.sort(reverse=True)

ret=0
s_list=[]

for i in range(N):
    n=L_list[i]
    for j in range(i+1,N):
        k=L_list[j]
        s=0
        for h in range(j+1,N):
            l=L_list[h]
            if l>n-k:
                s=s+1
            else:
                break
        s_list.append(s)
        ret=ret+s

print(ret)
print(s_list)