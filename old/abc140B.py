N=int(input())
A_list=[int(thing) for thing in input().split(" ")]
B_list=[int(thing) for thing in input().split(" ")]
C_list=[int(thing) for thing in input().split(" ")]
ret=0
P_B=0
for d in range(len(A_list)):
    tottano=A_list[d]-1
    if d!=0 and tottano!=N:
        print("A")
        if tottano==sakki+1:
            ret=ret+C_list[sakki]
    ret=ret+B_list[tottano]
    sakki=tottano
print(ret)