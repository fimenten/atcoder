H,W,K=[int(thing) for thing in input().split(" ")]
s=[]
[s.append(list(input())) for i in range(H)]

height=0
k=0
ret=[]
for h in s:
    kk=0
    string=""
    for char in h:
        if char=="#":
            k=k+1
            kk=k
            string=string+str(kk)
        else:string=string+str(kk)
    if string=="0"*W:
        ret.append(None)
    else:
        string=list(string)
        for i in range(W):
            if list(string)[W-1-i]==str(0):
                string[W-1-i]=string[W-i]
        ret.append(list(string))

    height=height+1
    kk=0


    #再帰でNoneを埋める
e=0
while True:
   if not type(ret[e])==type(None):
        for i in range(0,e+1):
            ret[i]=ret[e]
        ee=e+1
        while True:
            if ee==H:
                break

            if type(ret[ee])==type(None):
                ret[ee]=ret[e]
            else:
                e=ee
            ee=ee+1
        break
for h in ret:
    print(" ".join(h))