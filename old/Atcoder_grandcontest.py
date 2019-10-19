
H,W=[int(thing) for thing in list(str(input()).split(" "))]
banmen_list=[]
for h in range(H):
    banmen_list.append(list(str(input())))

def sousa(banmen,kaisu):
    rbanmen_list=banmen
    T=False
    for i in range(H):
        for j in range(W):
            if banmen[i][j]=="#":
                osen = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
                for y,x in osen:
                    if x<0 or y<0:
                        continue
                    if x>H-1 or y>W-1:
                        continue
                    if rbanmen_list[x][y]=="#":
                        continue
                    if banmen[x][y] == "#":
                        continue
                    rbanmen_list[x][y]="#"
                    T=True
    if T==False:
        if kaisu==0:
            print(kaisu)
        else:
            print(kaisu+1)
        return
    else:
        kaisu=kaisu+1
        sousa(rbanmen_list,kaisu)
sousa(banmen_list,0)