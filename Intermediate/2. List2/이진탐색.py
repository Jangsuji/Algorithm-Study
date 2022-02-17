'''
============================================
[입력]
3
400 300 350
1000 299 578
1000 222 888

[출력]
#1 A
#2 0
#3 A
============================================
'''

test_case = int(input())


def loop(l,r, page):
  cnt = 0
  while True:
    c=int((l+r)/2)
    if page < c:
      r = c
      cnt += 1
    elif page > c:
      l = c
      cnt += 1
    else:
      break
  return cnt

for t in range(test_case):
  P, A, B = map(int, input().split())
  cntA = loop(1,P,A)
  cntB = loop(1,P,B)
  if cntA-cntB < 0:
    print("#{0} A".format(t+1))
  elif cntA-cntB > 0:
    print("#{0} B".format(t+1))
  else:
    print("#{0} 0".format(t+1))