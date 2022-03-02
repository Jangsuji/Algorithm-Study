'''
============================================
[입력]
3
5 abac
9 ltsodjxzyc
21 jldgovukjf

[출력]
#1 a 2
#2 j 2
#3 j 4
============================================
'''

test_case = int(input())
for t in range(test_case):

    N, data_string = input().split()
    prefix_string = []

    while data_string:
        for j in range(len(data_string)):
            prefix_string.append(data_string[:j+1])
        data_string = data_string[1:]
    prefix_string = sorted(set(prefix_string))
    result = prefix_string[int(N)-1]

    print("#{} {} {}".format(t+1,result[0], len(result)))