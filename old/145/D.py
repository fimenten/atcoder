mod = 1000000007

import math
import sys

sys.setrecursionlimit(mod)

from operator import mul
from functools import reduce


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom//(10**9+7)

def junretsu(n,r):
    l=1
    for i in range(r+1,n+1):
        l= (l * i)%mod
    return l

def facto(n):
    l=1
    for i in range(1,n+1):
        l=(l*i)%(10**9+7)
    return l
X,Y=[int(thing) for thing in input().split(" ")]

def owari():
    print("0")
    exit()


def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y/2)**2 % mod
    else            : return power(x, y/2)**2 * x % mod

def diff(a,b):
    return a*power(b,1000000005)%mod
kk=2*X-Y
if kk<0:
    owari()
if kk%3 !=0:
    owari()

ll=2*Y-X

if ll<0:
    owari()
if ll%3 !=0:
    owari()


k=int(kk//3)
l=int(ll//3)
print(diff(junretsu(k+l,k),facto(l)))
