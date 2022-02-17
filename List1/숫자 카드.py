'''
============================================
[입력]
3
5
49679
5
08271
10
7797946543

[출력]
#1 9 2
#2 8 1
#3 7 3
============================================
'''

test_case = int(input())

for t in range(test_case):
  num = input()

  cards = input()
  cards = [int(i) for i in list(cards)]
  count={}

  for i in sorted(cards):
      try: count[i] += 1
      except: count[i]=1

  sorted_dict = sorted(count.items(), key = lambda item: item[1])
  print("#{0} {1} {2}".format(t+1, sorted_dict[-1][0], sorted_dict[-1][1]))