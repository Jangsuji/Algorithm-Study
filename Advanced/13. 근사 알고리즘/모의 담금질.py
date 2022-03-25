'''
============================================
[입력]
3
1000 0.1 0.8
1000 0.1 0.99
10000 0.0001 0.995

[출력]
#1 42
#2 917
#3 3675
============================================
'''

import math


test_case = int(input())
for t in range(test_case):

        T, T_end, k = map(float, input().split())
        cost_pre = 1000000  # 이전 비용
        cnt = 0

        while T > T_end:          # T_end가 될 때까지 반복

                cost_new = T     # 비용 계산

                diff = cost_new - cost_pre    # 새로운 비용과 이전 비용의 차이

                if diff < 0 or  math.e(-diff/T) > random(0,1):

                        cost_pre = cost_new    # 비용이 감소하거나 확률이 랜덤 값보다 더 크면 비용 갱신

                T = T * k                 # k : cooling factor
                cnt += 1
        print('#{} {}'.format(t+1,cnt))