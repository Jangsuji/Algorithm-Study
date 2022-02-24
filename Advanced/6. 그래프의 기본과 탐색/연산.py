'''
============================================
[입력]
3
2 7
3 15
36 1007

[출력]
#1 3
#2 4
#3 8
============================================
'''

test_case = int(input())
for t in range(test_case):

    N, M = map(int, input().split())
    cnt = 0
    while True:
        if M % 2 != 0:
            M -= 1
            cnt += 1
            if int(M) == N:
                break
        if M%2 == 0:
            M /= 2
            cnt += 1
            if int(M) == N:
                break

    print(cnt)

    print()











