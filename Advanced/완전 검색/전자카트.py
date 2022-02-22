'''
============================================
[입력]
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0

[출력]
#1 89
#2 96
#3 139
============================================
'''

import itertools


test_case = int(input())
for t in range(test_case):
    N = int(input())
    direction = range(2,N+1)
    candi = list(itertools.permutations(direction))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for route in candi:
        j = 1
        sum = 0
        for i in route:
            sum += matrix[j-1][i-1]
            j=i
        sum += matrix[j-1][0]
        result.append(sum)
    print("#{0} {1}".format(t + 1, min(result)))