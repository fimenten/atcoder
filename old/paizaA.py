H,W,N=[int(thing) for thing in input().split(" ")]
rec_list=[[int(i) for i in str(input()).split(" ")] for thing in range(N)]
Field=[]
for i in range(W):
    tate=["." for j in range(H)]
    Field.append(tate)

print(rec_list[0])
def fall(rec_info):
    h,w,x=rec_info
    x_list=[x+i for i in range(w)]

    for takasa in range(H):
        for ekkusu in x_list:
            if Field[ekkusu][H-takasa]=="#":
                break
        else:
            break
    y=H-takasa