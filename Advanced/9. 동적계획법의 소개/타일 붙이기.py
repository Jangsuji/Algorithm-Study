'''
============================================
[입력]
3
5
8
10

[출력]
#1 28
#2 277
#3 1278
============================================
'''


def fact(N):
  factorial_list = []
  if N == 1 or N == 0:
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
  for i in range(int(width/3) + 1):
    for j in range(int((width-3*i) / 2) + 1):
      data_dict = {}
      data_dict['tr'] = i
      data_dict['tw'] = j
      data_dict['one'] = int((width-3*i) - 2 * j)
      data_list.append(data_dict)

  for case in data_list:
    if case['tr'] == 0 and case['tw'] == 0:
      cnt += 1
    elif case['tw'] != 0:
      n = case['tr'] + case['tw'] + case['one']
      one = case['one']
      tw = case['tw']
      tr = case['tr']
      cnt += (fact(n) / fact(one) / fact(tw) / fact(tr)) * 2 ** tw
    elif case['tr'] != 0:
      n = case['tr'] + case['tw'] + case['one']
      r = case['tr']
      cnt += (fact(n) / fact(n - r) / fact(r))
  print("#{0} {1}".format(t + 1, int(cnt)))