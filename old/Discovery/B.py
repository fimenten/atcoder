N=int(input())
A_list=[int(thing) for thing in input().split(" ")]

Suu=sum(A_list)
S=Suu*0.5
import sys

sys.setrecursionlimit(2000)
def my_bisect(l:list,left_true=False):
    def bis(begin:int,end:int):
        # print("{}:{}".format(begin,end))
        if end-begin<=1:
            if begin==0:
                if A_list[0]>S:
                    return 0
                else:return 1
            #
            # print(sum(A_list[0:begin+1]))
            # print(sum(A_list[0:end+1]))
            if begin==0:
                B=A_list[begin+1]
            else:
                B=sum(A_list[0:begin+1])
            if B>S==True:
                return begin
            else:
                return end

        v=int((end+begin)/2//1)
        # print("v="+str(v))
        res=sum(A_list[0:v+1])>S
        # print(sum(A_list[0:v+1]))
        #
        # print(res)
        if not res:
            return bis(v,end)
        elif  res:
            return bis(begin,v)
        else:
            print("what")
    return bis(0,len(l)-1)

m=my_bisect(A_list)

# print(m)
if m==0:
    print(A_list[0])
else:
    if m==1:
        nagasa=A_list[0]
    else:
        nagasa=sum(A_list[:m])
    print(min(abs((nagasa+A_list[m])*2-Suu),abs(nagasa*2-Suu)))