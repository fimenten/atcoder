import collections
N,K,Q=[int(thing) for thing in input().split(" ")]
A_list=[int(input()) for thing in range(Q)]

c=collections.Counter(A_list)
cc={str(i):c[i] for i in c}
c=cc
for i in range(N):
    if str(i+1) in c:
        seikai=c[str(i+1)]
    else:
        seikai=0

    point=K-Q+seikai
    print(point)
    continue
    if point>0:
        print("Yes")
    else:
        print("No")
