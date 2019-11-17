import math
N=int(input())
end=int(math.sqrt(N)//1+1)
def func(i):
    d,m=divmod(N,i)
    if m==0:
        return i+d
    else:
        return 10**12+1
ret=min([func(i) for i in range(1,end)])-2
print(int(ret))

