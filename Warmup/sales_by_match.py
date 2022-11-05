from collections import Counter
def sockMerchant(n, ar):
    s=0
    for val in Counter(ar).values():
        s+=val//2
    return s
if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().strip().split()))
    result = sockMerchant(n, ar)
    print (result)
