def my_bisect(l:list,f,left_true=True):
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
        if res and left_true:
            return bis(v,end)
        elif not res and left_true:
            return bis(begin,v)
        elif res and not left_true:
            return bis(begin,v)
        elif not res and not left_true:
            return bis(v,end)
        else:
            print("what")
    return bis(0,len(l)-1)