s=input()
t=input()

if len(list(set(list(t))-set(list(s))))!=0:
    print("-1")
else:
    import copy
    def make_dict(s):
        s= str(s)
        ret={}
        for char_index in range(len(s)):
            char=list(s)[char_index]
            if char not in ret:
                ret[char]=[]
            ret[char].append(char_index)
        return ret
    dict_of_the_sentence=make_dict(s)
    s_len=len(s)
    t_len=len(t)
    ind_int=0
    insent_ind=0
    used={char:[] for char in dict_of_the_sentence}
    for char in list(t):
        while True:
            if not dict_of_the_sentence[char].__len__()==0:
                    temp_ind=dict_of_the_sentence[char].pop(0)
                    used[char].append(temp_ind)
                    if temp_ind>=insent_ind:
                        insent_ind=temp_ind
                        break
                    else:
                        pass
            else:
                ind_int=ind_int+s_len
                insent_ind=0
                for chars in used:
                    t_list=list(set(dict_of_the_sentence[chars])|set(used[chars]))
                    t_list.sort()
                    dict_of_the_sentence[chars]=t_list
                used = {chara: [] for chara in dict_of_the_sentence}

    ind_int=ind_int+insent_ind+1
    print(ind_int)