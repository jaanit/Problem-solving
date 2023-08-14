import math

a,b = map(int, input().split())
res = a*b
re = res // math.gcd(a,b)
print(re)
