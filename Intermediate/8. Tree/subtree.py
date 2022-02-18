'''
============================================
[입력]
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10

[출력]
#1 3
#2 1
#3 3
============================================
'''


test_case = int(input())
for t in range(test_case):
  sibiling1 = {}
  sibiling2 = {}
  result = []
  E,N = map(int, input().split())
  data_list = list(map(int, input().split()))
  for i in range(E):
    if data_list[i*2] in sibiling1:
      sibiling2[data_list[i * 2]] = data_list[i * 2 + 1]
    else:
      sibiling1[data_list[i*2]] = data_list[i*2+1]
  result.append(N)

