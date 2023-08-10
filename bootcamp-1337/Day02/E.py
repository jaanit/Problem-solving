import math

def calcul(A, B, C,mid):
    return A*mid + B*math.sin(mid) - C
T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    low = 0
    high = 10000
    while high - low > 1e-6:
        mid = (low + high) / 2
        if calcul(A, B, C,mid) > 0:
            high = mid
        else:
            low = mid
    print("{:.6f}".format(mid))