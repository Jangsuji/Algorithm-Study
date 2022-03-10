'''
============================================
[입력]
3
2 1 1
3 2 1
5 3 2

[출력]
#1 2
#2 3
#3 10
============================================
'''

def bino2(n,k):
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
    return B[n][k]

test_case = int(input())

for t in range(test_case):

    n,a,b = map(int, input().split())
    B = [[0 for _ in range(n+1)] for _ in range(n+1)]
    print("#{} {}".format(t+1,bino2(n,b)))