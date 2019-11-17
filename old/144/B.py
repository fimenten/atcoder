N=1
if N>81:
    print("No")
else:
    p_list=[9,8,7,6,5,4,3,2,1]
    for p in p_list:
        d,m=divmod(N,p)
        if d<10 and m==0:
            print("Yes")
            break
    else:print("No")