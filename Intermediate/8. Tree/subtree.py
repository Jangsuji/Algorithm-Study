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
  cnt = 0

  E,N = map(int, input().split())
  result = [N]
  data_list = list(map(int, input().split()))
  for i in range(E):
    if data_list[i*2] in sibiling1:
      sibiling2[data_list[i * 2]] = data_list[i * 2 + 1]
    else:
      sibiling1[data_list[i*2]] = data_list[i*2+1]

  while True:
    try:
      node = result.pop()
      cnt += 1
      if node in sibiling1:
        result.append(sibiling1[node])
      if node in sibiling2:
        result.append(sibiling2[node])
    except:
      break

  print("#{} {}".format(t+1,cnt))

