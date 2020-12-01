# problem link --> https://www.hackerrank.com/challenges/electronics-shop/problem?h_r=next-challenge&h_v=zen

def getMoneySpent(keyboards, drives, b):

    sum_bu = []
    for i in keyboards:
        for x in drives:
            z = i + x
            if z <= b:
                sum_bu.append(z)
            else:
                sum_bu.append(-1)
    return max(sum_bu)

if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent) + '\n')
