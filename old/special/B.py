kaisu=0
def OK(tup):
    if tup[0] <= tup[1]:
        return True
    else:return False
def trade(i,recipient):
    A=recipient[0]
    for j in range(0,i):
        k=i-j-1
        if k==-1:
            print("No")
            exit()
        tpp=tups[k]
        if OK((A,tpp[1])):
            B=tpp[0]
            tpp[0]=A
            recipient[0]=B
            break
    else:
        print("No")
        exit()


N=int(input())
tups=[[i,j] for i,j in zip([int(thing) for thing in input().split(" ")],[int(thing) for thing in input().split(" ")])]
tups.sort(reverse=True,key=lambda x:x[1])
for i in range(0,N):
    tup=tups[i]
    if OK(tup):
        pass
    else:
        trade(i,tup)
        kaisu=kaisu+1
        if kaisu > N - 1:
            print("No")
            exit()
print("Yes")