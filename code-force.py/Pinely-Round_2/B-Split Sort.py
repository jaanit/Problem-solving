
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    s = set()
    res = 0
    for i in l:
        s.add(i)
        if (i-1 in s):
            res += 1
    print(n - res - 1)