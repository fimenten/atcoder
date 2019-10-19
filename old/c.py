N=input()
S=input()

# #を検出してその右にある全ての.をシャープに変える。最も左側にあるシャープを見つけてそれより右にある.の個数を返す

def first(S):
    if "#" in set(S):
        ichi=S.index("#")
        return int(S.count(".",ichi+1,int(N)))
    else:
        return 0

# .を検出してその左にある＃を.に変える。最も右にある.を見つけてそれより左にある#を数える。
def second(S):
    if "." in set(S):
        ichi =S.rindex(".")
        return int(S.count("#",0,ichi-1))
    else:
        return 0
print(min([first(S),second(S)]))