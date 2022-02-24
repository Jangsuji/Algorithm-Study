'''
============================================
[입력]
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 2

[출력]
#1 3
#2 2
#3 3
============================================
'''

def BFS(G):
    Q = []
    visited = [0]*(N+1)
    v = 1
    Q.append(v)

    cnt = 1
    while Q:
        v = Q.pop(0)
        visited[v] = True
        for idx, val in enumerate(G[v]):
            if val == 1:
                if not visited[idx]:
                    Q.append(idx)
                    # visited[idx] = True
        if not Q and 0 in visited[1:]:
            Q.append(visited[1:].index(0)+1)
            cnt+=1
        elif 0 not in visited[1:]:
            break
    return cnt

test_case = int(input())
for t in range(test_case):

    N,M = map(int, input().split())
    application = list(map(int, input().split()))

    groups = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(M):
        a,b = application[2*i], application[2*i+1]
        groups[a][b] = 1
        groups[b][a] = 1
    cnt = BFS(groups)
    print("#{} {}".format(t+1,cnt))


