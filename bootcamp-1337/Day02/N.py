import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
n = int(input())
nbs = list(map(int, input().split()))

for num in nbs:
    sqrt_num = int(math.sqrt(num))
    if sqrt_num * sqrt_num == num and is_prime(sqrt_num):
        print("YES")
    else:
        print("NO")