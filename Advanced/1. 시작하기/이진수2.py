'''
============================================
[입력]
3
0.625
0.1
0.125

[출력]
#1 101
#2 overflow
#3 001
============================================
'''


test_case = int(input())
for t in range(test_case):

    bin = []
    dec = float(input())
    criteria = 0.5
    while True:
        residue = dec - criteria
        if residue > 0:
            bin.append(1)
            dec = residue
            criteria /= 2
        elif residue < 0:
            bin.append(0)
            criteria /= 2
        elif residue == 0:
            bin.append(1)
            d2b = ''.join(str(e) for e in bin)
            print("#{0} {1}".format(t + 1, d2b))
            break
        if len(bin)>12:
            print("#{0} overflow".format(t + 1))
            break

