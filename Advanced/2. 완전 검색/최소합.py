'''
============================================
[입력]
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1

[출력]
#1 15
#2 18
#3 33
============================================
'''

import itertools


test_case = int(input())
for t in range(test_case):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    direction = ['r']*(N-1) + ['d']*(N-1)
    candi = set(list(itertools.permutations(direction)))
    result = []

    for route in candi:
        row = 0
        column = 0
        sum = matrix[row][column]
        for i in route:
            if i == 'r':
               column += 1
            else:
               row += 1
            sum += matrix[row][column]
        result.append(sum)
    print("#{0} {1}".format(t+1, min(result)))

