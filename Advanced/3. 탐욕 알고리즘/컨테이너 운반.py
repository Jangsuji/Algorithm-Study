'''
============================================
[입력]
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13

[출력]
#1 8
#2 45
#3 84
============================================
'''

test_case = int(input())
for t in range(test_case):
    N, M = map(int, input().split())
    Wi = sorted(list(map(int, input().split())), reverse=True)
    Ti = sorted(list(map(int, input().split())), reverse=True)
    pop_list = []

    for i in range(min(N,M)):
        if Ti[i] < Wi[i]:
            pop_list.append(Wi[i])
            Ti.insert(i,0)
    print("#{0} {1}".format(t+1, sum(Wi[:M])-sum(pop_list)))
