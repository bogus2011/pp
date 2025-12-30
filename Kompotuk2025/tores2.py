from collections import defaultdict

n = 6
m = 10

crosses = set()

#rect => (id, x1,x2,y1,y2) (1, x11,y11,x12,y12) (2, x21,y21,x22,y22)
rects = set()
rects.add((1,1,1,2,4))
rects.add((2,2,1,4,5))
rects.add((3,3,2,5,6))
rects.add((4,1,7,3,9))
rects.add((5,2,8,5,10))
rects.add((6,5,7,6,10))

for r in rects:
    print(f"rect in procesiing {r}")
    for rr in rects:
        if r[0] == rr[0]:
            continue
        print(rr)
        if not (r[3] < rr[1] or r[1] > rr[3] or r[4] < rr[2] or r[2] > rr[4]): #x2a (x12) < x1b(x21) or x1a (x11) > x2b (x22) or y2a(y12) < y1b(y21) or y1a(y11) > y2b(y22)
            print(f"{r} crosses {rr}")
            if (r[0],rr[0]) in crosses or (rr[0],r[0]) in crosses:
                continue
            crosses.add((r[0],rr[0]))

print(crosses)

graph = defaultdict(set)
for a, b in crosses:
    graph[a].add(b)
    graph[b].add(a)

visited = set()
groups = []


for v in graph:
    if v not in visited:
        stack = [v]
        group = set()

        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            group.add(u)
            stack.extend(graph[u])

        groups.append(group)

print(groups)        


        


