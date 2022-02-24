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

test_case = int(input())
for t in range(test_case):

    N,M = map(int, input().split())
    application = list(map(int, input().split()))

    groups = [[i] for i in range(N+1)]
    for i in range(M):
        a,b = application[2*i], application[2*i+1]
        groups[a].append(b)
        groups[b] = [0]

    idx = 0
    while True:
        if 0 in groups[idx]:
            groups.pop(idx)
            idx -= 1
        idx +=1
        if idx == len(groups):
            break
    print("#{} {}".format(t+1,len(groups)))


