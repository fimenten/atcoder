M,N,K=[int(thing) for thing in input().split(" ")]
sups_dict={str(i):0 for i in range(M+1)}
sups_dict[-1]=N
enzetsu_list=[int(input()) for i in range(K)]
def enzetsu(j):
    j=str(j)
    if sups_dict[-1]!=0:
        sups_dict[-1]=sups_dict[-1]-1
        sups_dict[j]=sups_dict[j]+1
    for key in sups_dict:
        if j==key or key==-1:
            pass
        else:
            if sups_dict[key]!=0:
                sups_dict[key]=sups_dict[key]-1
                sups_dict[j]=sups_dict[j]+1
for f in enzetsu_list:
    enzetsu(f)
sups_dict[-1]=0
ma=max([sups_dict[thing] for thing in sups_dict])
vic_list=[thing for thing in sups_dict if sups_dict[thing]==ma]
for c in vic_list:
    print(c)
