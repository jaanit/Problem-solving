n = int(input())
matrix = []
for _ in range(n):
    l = list(map(int, input().split()))
    matrix.append(l)
roads = sum(matrix[i][j] for i in range(n) for j in range(i + 1, n))
print(roads)
