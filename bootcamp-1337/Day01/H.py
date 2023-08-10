t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    s = input()
    idx = 0
    while idx < n and int(s[idx]) >= d:
        idx += 1
    if idx == n:
        print(s + str(d))
    else:
        print(s[:idx] + str(d) + s[idx:])