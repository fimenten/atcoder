import math
import collections
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N=int(input())
strings=[str(sorted(input())) for a in range(N)]
c=collections.Counter(strings)
tp=c.most_common()
sums=0
for thing in tp:
    if thing[1]!=1:
        sums=sums+combinations_count(thing[1],2)
    else:break

print(sums)