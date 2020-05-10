N=int(input())

def hukano():
    print(":(")
def zeikomi(n):
    return n*1.08//1

N_min=N*9//10

k=N_min
while True:
    teika=int(zeikomi(k))
    if int(teika)==N:
        print(k)
        break
    elif teika<N:
        k=k+1
    else:
        hukano()
        break