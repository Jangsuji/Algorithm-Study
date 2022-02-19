'''
============================================
[입력]
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

[출력]
#1 4
#2 8
#3 6
============================================
'''

test_case = int(input())
for t in range(test_case):

  N, M = map(int, input().split())
  cheese = list(map(int, input().split()))
  cheese_list = []
  for i in range(M):
    cheese_list.append((i + 1, cheese[i]))
  pot = []
  cnt = 0

  while True:
    if len(pot) != N:
      try:
        pizza = cheese_list.pop(0)
        pot.insert(0, pizza)
      except:
        pot.insert(0, (100, 100))
        cnt += 1
    else:
      pizza = pot.pop()
      if pizza[1] // 2 != 0:
        pot.insert(0, (pizza[0], pizza[1] // 2))
    if cnt == N - 1:
      break

  a = [i for i in pot if i[0] != 100]
  print("#{0} {1}".format(t + 1, a[0][0]))