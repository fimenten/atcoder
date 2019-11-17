N,T=[int(thing) for thing in input().split(" ")]
l_list=[[int(thing) for thing in input().split(" ")] for i in range(N)]
[l.append(l[1]/l[0]) for l in l_list]
l_list.sort(key=lambda x:x[2],reverse=True)
t=0
val=0
for l in l_list:
    ti=l[0]
    val=l[1]
    if t+ti>=T-0.5:
        if t+ti<=T:
            t = t + ti
            val = val + l[1]
            break

    else:
        t=t+ti
        val=val+l[1]

