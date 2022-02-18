'''
============================================
[입력]
3
30
50
70

[출력]
#1 5
#2 21
#3 85
============================================
'''


def fact(N):
  factorial_list = []
  if N == 1:
    return 1
  else:
    result = fact(N - 1) * N
    factorial_list.append(result)
  return factorial_list[-1]


test_case = int(input())

for t in range(test_case):
  cnt = 0
  data_list = []
  width = int(input())
  for i in range(int(width / 20) + 1):
    data_dict = {}
    data_dict["b"] = i
    data_dict["a"] = int((width - 20 * i) / 10)
    data_list.append(data_dict)

  for case in data_list:
    if case['b'] == 0:
      cnt += 1
    elif case['a'] == 0:
      r = case['b']
      cnt += 2 ** r
    else:
      n = case['a'] + case['b']
      r = case['b']
      cnt += (fact(n) / fact(n - r) / fact(r)) * 2 ** r
  print("#{0} {1}".format(t + 1, int(cnt)))