N,K=[int(thing) for thing in input().split(" ")]
A_list=[int(i) for i in input().split(" ")]

def get_inv_num(l):
    l=list(l)
    ret=0
    for ind in range(len(l)):
        char=l[ind]
        for s_ind in range(len(l))[ind:]:
            if int(l[s_ind])<int(char):
                ret=ret+1
    return ret

def get_inv_external(l):
    import collections
    l=list(l)
    l_count=collections.Counter(l)
    ret=0
    memo={}
    for num in l:
        if str(num) in memo:
            ret=ret+memo[str(num)]
        else:
            ret_tmp=0
            for suuji in l_count:
                if int(suuji)<int(num):
                    ret_tmp=ret_tmp+l_count[suuji]
            memo[str(num)]=ret_tmp
            ret=ret+ret_tmp
    return ret
internal=get_inv_num(A_list)
external=get_inv_external(A_list)
n,ret=divmod(internal*K+external*(K-1)*K//2,10**9+7)
print(ret)