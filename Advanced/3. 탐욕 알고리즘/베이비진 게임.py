'''
============================================
[입력]
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3

[출력]
#1 0
#2 1
#3 2
============================================
'''

def baby_gin(cnt):
    flag = False
    for i,v in enumerate(cnt):
        if v == 3:
            flag = True
            break
        try:
            if cnt[i]>0 and cnt[i+1]>0 and cnt[i+2]>0:
                flag = True
        except:
            pass
    return flag




test_case = int(input())
for t in range(test_case):
    card = list(map(int, input().split()))
    cnt1 = [0]*10
    cnt2 = [0]*10
    for idx, val in enumerate(card):
        if idx % 2 == 0:
            cnt1[val] += 1
            flag = baby_gin(cnt1)
            if flag == True:
                print("#{0} 1".format(t+1))
                break
        else:
            cnt2[val] += 1
            flag = baby_gin(cnt2)
            if flag == True:
                print("#{0} 2".format(t+1))
                break
        if idx == 11:
            print("#{0} 0".format(t+1))