N,K=[int(thing) for thing in input().split(" ")]
H_list=[int(thing) for thing in input().split(" ")]
H_list=sorted(H_list,reverse=True)
fuckable=sum(H_list[0:K])
health_sum=sum(H_list)
need_attack=health_sum-fuckable
print(need_attack)