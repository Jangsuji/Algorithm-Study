'''
============================================
[입력]s
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

[출력]
#1 21
#2 11088
#3 1090
============================================
'''

test_case = int(input())

for t in range(test_case):
  n,m = map(int, input().split())
  results = [0]*(n-m+1)
  data_list = list(map(int, input().split()))

  for i in range(len(results)):
    results[i] = sum(data_list[i:i+m])
    result = sorted(results)[-1]-sorted(results)[0]
  print("#{0} {1}".format(t+1, result))