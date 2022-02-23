'''
============================================
[입력]
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24

[출력]
#1 4
#2 4
#3 5
============================================
'''

test_case = int(input())
for t in range(test_case):
    N = int(input())
    time_list = []
    time_table = []
    for _ in range(N):
        time = tuple(map(int,input().split()))
        time_list.append(time)

    time_list.sort(key=lambda x:x[1])
    criteria = time_list.pop(0)
    time_table.append(criteria)
    for time in time_list:
        if time[0] >= criteria[1]:
            time_table.append(time)
            criteria = time
    print("#{} {}".format(t+1, len(time_table)))











