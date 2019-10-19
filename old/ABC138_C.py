N=int(input())
values=[int(thing) for thing in input().split(" ")]
values.sort()
ret=0
for i in values:
    if ret!=0:
        ret=(i+ret)*0.5
    else:
        ret=i
print(ret)