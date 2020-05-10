import collections
N=int(input())
graph={i+1:[] for i in range(N)}
coloured=[0 for i in range(N+1)]
#↑0から始まってる（ただしkeyはそのまま使える）
node_list=[]

for i in range(N-1):
    node=tuple([int(thing) for thing in input().split(" ")])
    a=node[0]
    b=node[1]
    graph[a].append((b,i))
    graph[b].append((a,i))
# ranking=sorted(range(1,N),key=lambda x:len(graph[x]),reverse=True)

cc=1
ret=["" for i in range(N-1)]
def what_colour(cc,a_bit,b_bit):
    i=1
    while True:
        if (2**i&a_bit!=0) or (2**i&b_bit!=0):
            i=i+1
            continue
        else:
            return i,max(cc,i)
done_v=set()
q=collections.deque()
q.append(node[0])
done_v.add(node[0])

while q:
        i=q.popleft()
        for thing in graph[i]:
            j = thing[0]
            num = thing[1]

            c, cc = what_colour(cc, coloured[i], coloured[j])
            coloured[i] = coloured[i] + 2 ** c
            coloured[j] = coloured[j] + 2 ** c

            graph[j].remove((i, num))
            ret[num] = c
            if j not in done_v:
                q.append(j)
                done_v.add(j)


print(cc)
for thing in ret:
    print(thing)

    #処理したらgraphから消してcolourdにビットで（2**色）を加算。処理する前にビット積（&が0になるか確かめる）