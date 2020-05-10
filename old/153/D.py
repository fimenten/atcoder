import math


log2=math.log2
H=int(input())
n=math.floor(log2(H))
print(2**(n+1)-1)