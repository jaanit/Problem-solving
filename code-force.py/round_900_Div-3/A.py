t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    if k in l:
        print("YES")
    else:
        print("NO")