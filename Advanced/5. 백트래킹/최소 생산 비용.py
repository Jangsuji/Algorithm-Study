'''
============================================
[입력]
3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4

[출력]
#1 63
#2 78
#3 129
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





