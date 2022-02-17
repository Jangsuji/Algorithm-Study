'''
============================================
[입력]
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

[출력]
#1 3
#2 0
#3 4
============================================
'''


test_case = int(input())

for t in range(test_case):
  k,n,m = map(int, input().split())
  ori_k = k

  charging = list(map(int, input().split()))
  distance_list = [charging[i]-charging[i-1] for i in range(1, len(charging))]
  distance_list.append(n-charging[-1])

  cnt = 0
  for i in range(n+1):
    load = i
    if load in charging:
      if k<distance_list[0] and k != -1:
          k=ori_k
          cnt += 1
      distance_list.pop(0)
    if k == -1:
      cnt = 0
      break
    k -= 1
  print("#{0} {1}".format(t+1, cnt))