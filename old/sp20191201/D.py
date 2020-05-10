import itertools

N=int(input())
S=[int(thing) for thing in list(input())]
kes=N-3
pass_set=set([])
def passkosu(k):
    num = 0

    if k in S[0:N-1]:
        l_left=S.index(k)
        for l in range(0,10):
            if l in S[l_left+1:N-1]:
                l_center=S[l_left+1:].index(l)+l_left+1
                dif=len(set(S[l_center+1:]))
                num=num+dif
    return num

print(sum([passkosu(i) for i in range(0,10)]))