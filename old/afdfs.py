H,W=[int(thing) for thing in list(str(input()).split(" "))]
banmen_list=[]
for h in range(H):
    banmen_list.append(list(str(input())))


def issimple(string):
    if "#" in string and "." in string:
        return False
    else:
        return True

comp=[]
def bunkatsu(banmen,kaisu):
    h=len(banmen)
    w=len(banmen[0])
    if issimple("".join(banmen)):
        return kaisu
    for i in range(h-1):
        ban1=[banmen[k] for k in range(i)]
        ban2=[banmen[i+j] for j in range(h-i)]
        