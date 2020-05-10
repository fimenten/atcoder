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

def abstract_bisect(l:list,evaluate_function:callable):
    left_bool=evaluate_function(l[0])
    def evaluate_number(i):
        return evaluate_function(l[i])

    def bis(begin_num:int,end_num:int):
        if end_num-begin_num<=1:
            if evaluate_number(end_num)==left_bool:
                return end_num
            else:
                return begin_num
        else:
            center_num=int((begin_num+end_num)//2)
            centere_bool=evaluate_number(center_num)
            if centere_bool==left_bool:
                return bis(begin_num=center_num,end_num=end_num)
            else:
                return bis(begin_num=begin_num,end_num=center_num)
    return bis(0,len(l)-1)

