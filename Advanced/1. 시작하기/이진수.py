'''
============================================
[입력]
3
4 47FE
5 79E12
8 41DA16CD

[출력]
#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101
============================================
'''

def hex2bin(hex):
    bin = []
    try:
        for i in range(4):
            quotient, remainder = int(hex)//2, int(hex)%2
            bin.append(remainder)
            hex = quotient
        aggregation = list(reversed(bin))
        binary = ''.join(str(e) for e in aggregation)
        return binary
    except:
        if hex =='F':
            return '1111'
        elif hex =='E':
            return '1110'
        elif hex =='D':
            return '1101'
        elif hex =='C':
            return '1100'
        elif hex =='B':
            return '1011'
        else:
            return '1010'


test_case = int(input())
for t in range(test_case):

    result = []
    N, hex = input().split()
    for i in range(int(N)):
        temp = hex2bin(hex[i])
        result.append(temp)
    h2d = ''.join(str(e) for e in result)
    print("#{0} {1}".format(t + 1, h2d))
