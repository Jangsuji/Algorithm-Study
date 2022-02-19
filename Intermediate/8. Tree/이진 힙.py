'''
============================================
[입력]
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40

[출력]
#1 7
#2 5
#3 65
============================================
'''
import math

test_case = int(input())
for t in range(test_case):
  N = int(input())
  h = int(math.log2(N))
  data_list = list(map(int, input().split()))
  data_list.insert(0,0)


  for i in range(2, N+1):
    for _ in range(N):
      if data_list[i]<data_list[i//2]:
        a = data_list[i//2]
        data_list[i//2] = data_list[i]
        data_list[i] = a
      i = i//2

  ances_sum = 0
  for _ in range(h):
    N = N // 2
    ances_sum += data_list[N]

  print("#{0} {1}".format(t+1,ances_sum))