MOD = 10**9 + 7

def bm(a, b):
    if b == 0 or b == a:
        return 1
    
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    
    for i in range(a + 1):
        dp[i][0] = 1
        for j in range(1, min(i, b) + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
    
    return dp[a][b]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    result = bm(a, b)
    print(result)
