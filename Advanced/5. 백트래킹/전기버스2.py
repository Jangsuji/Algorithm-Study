'''
============================================
[입력]
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1

[출력]
#1 1
#2 2
#3 5
============================================
'''

test_case = int(input())
for t in range(test_case):

    capacity = list(map(int, input().split()))
    i = 1
    battery = capacity[1]
    cnt = 0

    while True:
        i += 1
        battery -= 1
        if battery == 0 and i != len(capacity):
            if capacity[i-1]-1 > capacity[i]:
                i -= 1
                battery = capacity[i]
            else:
                battery = capacity[i]
            cnt += 1
        elif i == len(capacity):
            break

    print("#{} {}".format(t+1,cnt))



