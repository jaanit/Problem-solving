import math

n = int(input())
l = list(map(int, input().split()))
res = l[0]
for i in range(1, len(l)):
    res = math.gcd(res, l[i])
print(res)