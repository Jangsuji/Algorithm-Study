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