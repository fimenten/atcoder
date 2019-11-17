import random
N=int(2000)
L_list=[random.randint(a=1,b=1000) for i in range(N)]
L_list.sort(reverse=True)
print(L_list)
ret=0
s_list=[]
def my_bisect(l:list,f):
    def bis(begin:int,end:int):
        # print("{}:{}".format(begin,end))
        if end-begin<=1:
            if f(l[end]) ==True:
                return end
            elif f(l[begin])==True:
                return begin
            else:
                return -1
        v=int((end+begin)/2//1)
        res=f(l[v])
        if res:
            return bis(v+1,end)
        else:
            return bis(begin+1,v)

    return bis(0,len(l)-1)
for i in range(N):
    n=L_list[i]
    diff=0
    for j in range(i+1,N-1):
        k=L_list[j]
        m=n-k
        l=L_list[j+1:N]
        s=my_bisect(l,lambda x:x>m)+1
        s_list.append(s)
        if s==0:
            break
        else:diff=diff+s
    if diff==0:
        break
    ret=ret+diff
print(ret)
