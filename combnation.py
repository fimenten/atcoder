#累乗を計算するとき、**演算子よりもpowを使うと早い。powの３つ目の引数にmodを指定できる。
#10**9+7は自力で計算し、直接値を記載したほうがいい。



mod = 1000000007

def modchoose(n, a,mod):
    x = 1
    y = 1
    if n/2 < a:
        a = n - a
    for i in range(a):
        x *= n - i
        if x > mod:
            x %= mod
        y *= a - i
        if y > mod:
            y %= mod
    val = x * pow(y, mod-2, mod) % mod
    return val
