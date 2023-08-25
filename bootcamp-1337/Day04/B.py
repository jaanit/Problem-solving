def solve():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    l = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                l.append((i + 1, j + 1))
    
    for edge in l:
        print(edge[0], edge[1])
if __name__ == "__main__":
    solve()
