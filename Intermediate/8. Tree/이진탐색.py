'''
============================================
[입력]s
3
6
8
15

[출력]
#1 4 6
#2 5 2
#3 8 14
============================================
'''

test_case = int(input())
for t in range(test_case):

    array_list = []
    N, M = map(int, input().split())
    for i in range(M):
        array_list.append(list(map(int, input().split())))
    linked_array = array_list[0]

    for array in array_list[1:M]:
        for idx, val in enumerate(linked_array):
            if val > array[0]:
                for i in list(reversed(array)):
                    linked_array.insert(idx, i)
                    # print(linked_array)
                break
            elif idx == len(linked_array) - 1:
                linked_array.extend(array)
                break

    answer = list(reversed(linked_array))[:10]
    print("#{0}".format(t + 1), end=" ")

    for i, num in enumerate(answer):
        if i == len(answer) - 1:
            print("{0}".format(num))
        else:
            print("{0} ".format(num), end="")