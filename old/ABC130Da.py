N,K=[int(thing) for thing in input().split(" ")]
a_list=[int(thing) for thing in input().split(" ")]

kosu=0

base=0
s=0

for a in range(N):
    s=s+a_list[a]
    if s>=K:
        kosu=kosu+N-a+2
        begin = 0
        end = a
        break
import copy
while True:
    print("{} {}".format(begin,kosu))
    s=s-a_list[begin]
    k=copy.copy(kosu)
    while True:
        if s>=K:
            kosu=kosu+N-begin+2
            break
        else:
            end=end+1
            if end<N:
                s=s+a_list[end]
            else:break
    begin=begin+1
    if k==kosu:
        break
    if begin>=N:
        break
    if end>N:
        break

print(kosu)