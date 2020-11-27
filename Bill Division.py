def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    x = sum(bill)
    ave = x / 2
    if b > ave :
        sub = b - ave
        print(int(sub))
    else:
        print('Bon Appetit')
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
