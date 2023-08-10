n = int(input())
res = (n * (n + 1)) // 2
if res % 2:
    print("NO")
else:
    print("YES")
    res //= 2
    s = set()
    for i in range(n, 0, -1):
        if res >= i:
            res -= i
            s.add(i)
    print(len(s), end=" ")
    for k in s:
        print(k, end=" ")
    print(n - len(s), end=" ")
    for i in range(1, n + 1):
        if i not in s:
            print(i, end=" ")
    print()