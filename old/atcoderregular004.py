def first():
    import math
    N=int(input())
    zahyo_list=[(int(thing[0]),int(thing[1])) for thing in [str(input()).split(" ") for i in range(N)]]
    max=0
    def get_distance(x1, y1, x2, y2):
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return d
    for i in range(N-1):
        for j in range(N-i):
            s=i+j
            d=get_distance(zahyo_list[i][0],zahyo_list[i][1],zahyo_list[s][0],zahyo_list[s][1])
            if d>max:
                max=d
    print(max)


N=int(input())
distance_list=[int(input()) for i in range(N)]
def func(gmin,gmax,n):
    if n>=gmin and n<=gmax:
        rmin=0
        rmax=gmax+n
        return rmin,rmax
    vals=[abs(gmin-n),abs(gmax-n),abs(gmax+n)]
    return min(vals),max(vals)
gmin=distance_list[0]
gmax=gmin

for dis in distance_list:
    gmin,gmax=func(gmin,gmax,dis)
print(gmin)
print(gmax)
