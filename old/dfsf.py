N=int(input())
B_list=[int(thing) for thing in input().split(" ")]
a_sum=0
for i in range(N):
    if i==0:
        a_sum=a_sum+B_list[0]
    else:
        if i==N-1:
            a_sum=a_sum+B_list[N-2]
        else:
            a_sum=a_sum+min(B_list[i],B_list[i-1])
print(a_sum)