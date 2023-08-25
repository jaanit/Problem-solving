t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = 10 - n
    print(k * (k - 1) * 3)
