# n ----> number of nodes
# m ----> number of edges
n, m = tuple(map(int, input().split()))

adjlist = [[] for i in range(n+1)]

for i in range(0, m):
    # u, v are edges
    # w is weight
    u,v,w = map(int, input()..strip().split()))
    adjlist[u].append([v,w])
    adjlist[v].append([u,w])

