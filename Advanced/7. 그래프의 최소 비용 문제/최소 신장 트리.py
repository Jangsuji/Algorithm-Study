'''
============================================
[입력]
3
2 3
0 1 1
0 2 1
1 2 6
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
#2 13
#3 22
============================================
'''

def MST_PRIM(G,s):
    key = [100]*(V+1)
    pi = [None]*(V+1)
    visited = [False]*(V+1)
    key[s] = 0

    for _ in range(V+1):
        minIndex = -1
        min = 100
        for i in range(V+1):
            if not visited[i] and key[i] < min:
                min = key[i]
                minIndex = i
        visited[minIndex] = True
        for v, val in enumerate(G[minIndex]):
            if not visited[v] and val < key[v]:
                key[v] = val
                pi[v] = minIndex
    return key



test_case = int(input())
for t in range(test_case):

    V,E = map(int,input().split())
    graph = [[100 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        n1,n2,w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w
    key = MST_PRIM(graph,0)
    print("#{} {}".format(t+1,sum(key)))