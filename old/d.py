N=int(input())
a=[int(input()) for i in range(N)].sort()
su=sum(a)
#すべての組み合わせのリストと可能な三角形の集合を作り、前者の要素のうち後者にある物の数を返す。

bool_list=[]
A,B,C=0,0,0

#i項目を選んだかどうかで再帰する関数
def saiki(i,A,B,C):
    if judge(A,B,C)!=True:
        return
    if i==N:
        bool_list.append(True)
        return
    suuchi=a[i]
    saiki(i+1,A+suuchi,B,C)
    saiki(i+1,A,B+suuchi,C)
    saiki(i+1,A,B,C+suuchi)

#与えられた3つの数について三角不等式を満たすかboolを返す

def judge(n,m,l):
    if n>=su:
        return False
    if m>=su:
        return False
    if l>=su:
        return False
    return True

saiki(0,A,B,C)

print(bool_list.count(True)%998244353)