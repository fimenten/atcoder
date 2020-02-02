A,B,X=[int(thing) for thing in input().split(" ")]


def nedan(n):
    return int(A*n+B*len(str(n)))

def bisect(begin,end):
    if abs(begin-end)<=1:
        if nedan(end)<=X:
            return end
        else:
            return begin
    else:
        center=(begin+end)//2
        if nedan(center)<=X:
            return bisect(center,end)
        else:
            return bisect(begin,center)
N=bisect(0,10**9)
print(N)