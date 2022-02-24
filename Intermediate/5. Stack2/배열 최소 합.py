'''
============================================
[입력]
4
4
10 3 2 1
10 2 5 1
10 2 5 6
4 10 10 10
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

[출력]
9
#1 8
#2 14
#3 9
============================================
'''

import itertools

test_case = int(input())
for t in range(test_case):

    N = int(input())
    array_list = [list(map(int, input().split())) for _ in range(N)]

    arr = range(N)
    nPr = itertools.permutations(arr,N)

    results = []

    for i in nPr:
        a = 0
        for idx,val in enumerate(i):
            a += array_list[idx][val]
        results.append(a)
    print("#{} {}".format(t+1, min(results)))