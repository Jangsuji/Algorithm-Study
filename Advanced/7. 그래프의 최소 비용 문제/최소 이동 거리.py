'''
============================================
[입력]
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

[출력]
#1 2
#2 4
#3 10
============================================
'''

def Dijkstra(G,r):
    D = [100]*(V+1)
    P = [None]*(V+1)
    visited = [False]*(V+1)
    D[r] = 0

    for _ in range(V+1):
        minIndex = -1
        min = 100
        for i in range(V+1):
            if not visited[i] and D[i] < min:
                min = D[i]
                minIndex = i
        visited[minIndex] = True
        for v, val in enumerate(G[minIndex]):
            if not visited[v] and D[minIndex]+val < D[v]:
                D[v] = D[minIndex]+val
                P[v] = minIndex
    return D


test_case = int(input())
for t in range(test_case):

    V,E = map(int,input().split())
    graph = [[100 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        n1,n2,w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w
    D = Dijkstra(graph,0)
    print("#{} {}".format(t+1,D[V]))