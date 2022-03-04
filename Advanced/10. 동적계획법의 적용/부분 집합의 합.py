'''
============================================
[입력]
3
10 7
10 53
100 5050

[출력]
#1 5
#2 1
#3 1
============================================
'''

test_case = int(input())
for t in range(test_case):

    N, K = map(int, input().split())
    set = [[7]]
    i = 0
    while True:
        sub = set[i][0]
        j = 1
        subset = []
        while True:
            if j not in subset:
                subset.extend([sub-(j),j])
                j += 1
            else:
                break
        subset = [[subset[i],subset[i+1]] for i in range(int(len(subset)/2))]
        set.append(subset)
        i+=1
    print(a)

