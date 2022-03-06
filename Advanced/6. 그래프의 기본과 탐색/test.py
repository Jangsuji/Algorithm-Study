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
import math


def serching(residue,cnt):
    global best

    if cnt>=best:
        return
    if residue == 0:
        best = cnt
        return

    elif residue > 0:
        b = round(math.log2(residue) * (+1))
        serching(residue - (2 ** b*(+1)),cnt+1)
    else:
        b = round(math.log2(residue*(-1)))
        if b <= a:
            serching(residue - (2 ** b * (-1)),cnt+1)

        if residue <= -10:
            b = round(math.log2(residue / (-10)))
            if a < b:
                b = a
            serching(residue - (2 ** b *(-10)),cnt+1)



test_case = int(input())
for t in range(test_case):
    N, M = map(int, input().split())

    a = round(math.log2(M / N))
    residue = M - (2 ** a * N)

    try:
        if a<round(math.log2(residue * (+1))):
            a = a+1
            residue = M - (2 ** a * N)
    except:
        pass

    best = 100

    serching(residue,cnt=a)
    print("#{} {}".format(t+1,best))









