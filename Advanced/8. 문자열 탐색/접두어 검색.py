'''
============================================
[입력]
2
3 3
able
abl
abroad
ab
abo
a
3 5
people
water
night
wa
h
country
ni
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
    for i in B:
        for j in A:
            if list(i) == list(j)[:len(list(i))]:
                cnt += 1
                break

    print("#{} {}".format(t+1,cnt))