N=int(input())
H_list=[int(thing) for thing in input().split(" ")]
ret=-1
cur=pow(10,9)
ret_list=[]
for h in H_list:
    if h<=cur:
        ret=ret+1
    else:
        ret_list.append(ret)
        ret=0
    cur=h
ret_list.append(ret)
print(max(ret_list))