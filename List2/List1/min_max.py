'''
============================================
[입력]
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

[출력]
#1 630739
#2 740510
#3 838110
============================================
'''

test_case = int(input())
data_dict = []

for i in range(test_case):
  number = int(input())
  data_list = list(map(int, input().split()))
  results = max(data_list) - min(data_list)
  data_dict.append((i,results))

data_dict = dict(data_dict)
for key, value in data_dict.items():
  print("#{0} {1}".format(key+1, value))