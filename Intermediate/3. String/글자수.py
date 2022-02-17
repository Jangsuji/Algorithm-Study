'''
============================================
[입력]
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW

[출력]
#1 2
#2 1
#3 3
============================================
'''

test_case = int(input())


for t in range(test_case):
  data_dict={}
  str1 = input()
  str2 = input()

  for i in range(len(str1)):
    data_dict[str1[i]] = str2.count(str1[i])
    selected_dict = max(data_dict.items(), key = lambda item: item[1])

  print("#{0} {1}".format(t+1,selected_dict[1]))