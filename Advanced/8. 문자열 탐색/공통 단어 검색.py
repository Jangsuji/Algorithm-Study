'''
============================================
[입력]
2
3 3
book
home
study
right
home
study
3 5
people
water
night
water
hand
country
night
people

[출력]
#1 2
#2 3
============================================
'''

test_case = int(input())
for t in range(test_case):

    N, M = map(int, input().split())
    A = [None]*N
    B = [None]*M

    for i in range(N):
        A[i] = input()
    for i in range(M):
        B[i] = input()

    cnt = 0
    for i in A:
        if i in B:
            cnt += 1

    print("#{} {}".format(t+1,cnt))


