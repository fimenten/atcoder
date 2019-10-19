M,D=[int(thing) for thing in input().split(" ")]
ret=0
for i in range(D):
    d=i+1
    d_10,d_1=divmod(d,10)
    if d_10<2 or d_1<2:
        continue
    product=int(d_10*d_1)
    if product<=M:
        ret=ret+1
print(ret)