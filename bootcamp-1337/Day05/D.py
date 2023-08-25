mod = 10**9 + 7
def multiply(a, b):
    return([[(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod],
            [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod]])

def power(matrix, exp):
    if exp == 1:
        return matrix
    if exp % 2 == 0:
        half_power = power(matrix, exp // 2)
        return multiply(half_power, half_power)
    else:
        return multiply(matrix, power(matrix, exp - 1))
n = int(input())
if n <=1:
    print(n)
else:
    matrix = [[1, 1], [1, 0]]
    l = power(matrix, n - 1)
    print(l[0][0])

