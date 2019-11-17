import math
N=int(input())
f_list=[[int(thing) for thing in input().split()] for i in range(N)]

def distance(f_1,f_2):
    return math.sqrt((f_1[0]-f_2[0])**2+(f_1[1]-f_2[1])**2)
l=[]
for i in range(N-1):
    for j in range(i+1,N):
        l.append(distance(f_list[i],f_list[j]))
print((N-1)*sum(l)/len(l))