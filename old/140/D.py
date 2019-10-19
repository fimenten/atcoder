import heapq
N,M=[int(thing) for thing in input().split(" ")]
A_list=[int(thing)*(-1) for thing in input().split(" ")]
heapq.heapify(A_list)
for aaaaa in range(M):
    thing =heapq.heappop(A_list)/2
    heapq.heappush(A_list,thing)
print(int(sum([thing*-1//1 for thing in A_list])))
