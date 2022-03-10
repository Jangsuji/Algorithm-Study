'''
============================================
[입력]
2
10 4
6 12
5 10
5 15
4 6
12 5
7 20
3 10
5 3
3 8
6 15

[출력]
#1 25
#2 33
============================================
'''


def knapsack():
    for i in range(m+1):
        K[i][0] = 0
    for w in range(n+1):
        K[0][w] = 0

    for i in range(1,m+1):
        for w in range(1,n+1):
            if weight[i]>w:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(K[i-1][w-weight[i]]+value[i],K[i-1][w])
    return K[m][n]


test_case = int(input())
for t in range(test_case):

    n, m = map(int, input().split())
    weight = [None] * (m+1)
    value = [None] * (m+1)
    K = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m):
        w, v = map(int, input().split())
        weight[i+1] = w
        value[i+1] = v

    print("#{} {}".format(t+1,knapsack()))
