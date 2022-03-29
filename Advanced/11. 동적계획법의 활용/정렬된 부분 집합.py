'''
============================================
[입력]
3
5 1 5 3 4 2
5 4 3 5 1 2
10 2 9 5 1 10 6 3 4 8 7

[출력]
#1 3
#2 2
#3 4
============================================
'''

test_case = int(input())
for t in range(test_case):

        subset = list(map(int, input().split()))
        N = subset.pop(0)
        subset.insert(0,0)
        opt = list(range(0,N+1))
        metrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
        
        for i in opt[1:]:
                for j in opt[1:]:
                        if subset[i] == opt[j]:
                                metrix[i][j] = metrix[i-1][j-1]+1
                        else:
                                metrix[i][j] = max(metrix[i-1][j],metrix[i-1][j-1],metrix[i][j-1])
        print('#{} {}'.format(t+1,metrix[-1][-1]))