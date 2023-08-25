def dfs(s, mat, vis):
    if vis[s]:
        return
    vis[s] = True
    for i in range(len(mat[s])):
        if mat[s][i] and not vis[i]:
            dfs(i, mat, vis)

def solve():
    n = int(input())
    ret = 0
    v = 0
    mat = []
    vis = [False] * n
    
    for i in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
        ret += sum(row)
    
    dfs(0, mat, vis)
    v = sum(vis)
    
    if (ret + 1) // 2 == n - 1 and v == n:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()