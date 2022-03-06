'''
============================================
[입력]
3
2 7
3 15
36 1007

[출력]
#1 3
#2 4
#3 8
============================================
'''
def CoinChange(choice, num, N):
    global best

    if best <= num:
        return
    else:
        for i in range(len(coin)):
            if choice[num-1] == '+1' and coin[i] == '-1':
                pass
            elif choice[num-1] == '-1' and coin[i] == '+1':
                pass
            elif choice[num-2] == '*2' and coin[i] != '*2' and coin[i] == choice[num-1]:
                pass
            else:
                choice[num] = coin[i]
                money = N
                for j in choice[:num+1]:
                    if j == '+1':
                        money += 1
                    elif j == '-1':
                        money -= 1
                    elif j == '*2':
                        money *= 2
                    elif j == '-10':
                        money -= 10
                if money == M:
                    best = num
                    print(choice)
                    break
                if best <= num:
                    return
                else:
                    CoinChange(choice, num+1, N)



test_case = int(input())
for t in range(test_case):
    N, M = map(int, input().split())
    coin = ['+1','-1','*2','-10']#[10,50,100,400,500]
    best = 13
    choice = [0]*13
    CoinChange(choice,0,N)
    print("#{} {}".format(t+1,best+1))