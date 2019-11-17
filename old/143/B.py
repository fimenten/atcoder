N=int(input())
d_list=[int(thing) for thing in input().split(" ")]

dd=sum([x*x for x in d_list])
s=sum(d_list)
S=s*s
ret=int(0.5*(S-dd))
print(ret)