H,N=[int(thing) for thing in input().split(" ")]
attack_maryoku_list=[tuple([int(thing) for thing in input().split(" ")]) for i in range(N)]


def abstract_bisect(l: list, evaluate_function: callable):
    left_bool = evaluate_function(l[0])

    def evaluate_number(i):
        return evaluate_function(l[i])

    def bis(begin_num: int, end_num: int):
        if end_num - begin_num <= 1:
            if evaluate_number(end_num) == left_bool:
                return end_num
            else:
                return begin_num
        else:
            center_num = int((begin_num + end_num) // 2)
            centere_bool = evaluate_number(center_num)
            if centere_bool == left_bool:
                return bis(begin_num=begin_num, end_num=center_num)
            else:
                return bis(begin_num=center_num, end_num=end_num)

    return bis(0, len(l) - 1)


def cost_performance(tup):
    return tup[0]/tup[1]
attack_maryoku_list.sort(reverse=True,key=cost_performance)

def can_kill(maryoku):
    def choose_best_magic(mp):
        i=0
        for tup in attack_maryoku_list:

            if tup[1] <= mp:
                print(i)
                return True, tup

            i+=1
        return False, (0,)

    Health=H
    mp=int(maryoku)
    while True:
        able,tup=choose_best_magic(mp)
        if not able:
            return False
        else:
            attack=tup[0]
            maryoku=tup[1]
            mp=mp-maryoku
            if mp<=0:
                return False
            Health=Health-attack
            if Health<=0:
                return True


for i in range(1,10):
    print(i)
    print(can_kill(i))