N,K=[int(thing) for thing in input().split(" ")]
a_list=[int(thing) for thing in input().split(" ")]
kosu=0
s_0=sum(a_list)

for i in range(N):
    if i==0:
        s=s_0
    else:
        s=s-a_list[i-1]

    if s>=K:
        s_1=s
        kosu=kosu+1
        for j in range(N-i):
            s_1=s_1-a_list[N-j-1]
            if s_1>=K:
                kosu=kosu+1
            else:break
print(kosu)