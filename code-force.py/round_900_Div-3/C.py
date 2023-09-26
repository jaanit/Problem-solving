t = int(input())
for i  in range(t):
    n,k,x= map(int,input().split())
    l = k * (k + 1) / 2
    r = l + (n - k) * k
    if x >= l and x <= r:
        print("YES")
    else:
        print("NO")