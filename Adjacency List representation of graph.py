# n ----> number of nodes
# m ----> number of edges
n, m = tuple(map(int, input().split()))

adjlist = [[] for i in range(n+1)]

for i in range(0, m):
    # Take input of all the edges
    x, y = tuple(map(int, input().split()))
    adjlist[x].append(y)
    adjlist[y].append(x)
print("Adjacency list of above graph is given by: ")
for i in range(1, n + 1):
    print(i,end="->")
    for j in adjlist[i]:
        print(j,end=" ")
    print()

'''
Input: -
7 7
1 2
1 3
2 4
2 5
2 6
2 7
7 3

Output: -
Adjacency list of above graph is given by: 
1->2 3 
2->1 4 5 6 7 
3->1 7 
4->2 
5->2 
6->2 
7->2 3

'''
