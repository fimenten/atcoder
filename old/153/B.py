H,N=[int(thing) for thing in input().split(" ")]
A_list=[int(thing) for thing in input().split(" ")]

Attack_sum=sum(A_list)
if H>Attack_sum:
    print("No")
else:
    print("Yes")