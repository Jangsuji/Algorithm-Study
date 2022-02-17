'''
============================================
[입력]
3
3 10
5527 731 31274
5 12
18140 14618 18641 22536 23097
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907

[출력]
#1 731
#2 18641
#3 2412
============================================
'''

test_case = int(input())
for t in range(test_case):

  N, M = map(int, input().split())
  data_list = list(map(int, input().split()))

  for i in range(M):
    data_list.append(data_list[0])
    del data_list[0]
  print("#{0} {1}".format(t + 1, data_list[0]))