'''
============================================
[입력]
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962

[출력]
#1 3
#2 845
#3 1801
============================================
'''

test_case = int(input())
for t in range(test_case):

  N, M, L = map(int, input().split())
  data_list = [0]*(N+1)
  for _ in range(M):
    idx, value = map(int, input().split())
    data_list[idx] = value

  for i in reversed(list(range(N-M))):
    try:
      data_list[i+1] = data_list[2*(i+1)]+data_list[2*(i+1)+1]
    except:
      data_list[i + 1] = data_list[2 * (i + 1)]
  print("#{0} {1}".format(t+1,data_list[L]))

