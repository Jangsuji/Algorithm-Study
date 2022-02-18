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


test_case = int(input())
for t in range(test_case):
  N,M,L = map(int, input().split())
  data_list = list(map(int, input().split()))
  for i in range(M):
    idx,val = map(int, input().split())
    data_list.insert(idx,val)
  print("#{0} {1}".format(t+1,data_list[L]))