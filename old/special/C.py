import collections
N=int(input())
D_list=[int(thing) for thing in input().split(" ")]
maxx=max(D_list)
if D_list[0] !=0:
    print(0)
    exit()
C=collections.Counter(D_list)
if C[0] != 1:
    print(0)
    exit()

ret=1
for i in range(0,maxx):
    if maxx-i not in C:
        print(0)
        exit()
    if maxx-i==0:
        pass
    else:
        ret=ret*C[maxx-i-1]**C[maxx-i]

print(ret%998244353)