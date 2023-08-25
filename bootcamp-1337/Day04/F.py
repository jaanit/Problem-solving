def dfs(s, mat, vis):
    if vis[s]:
        return
    vis[s] = True
    for i in range(len(mat[s])):
        if mat[s][i] and not vis[i]:
            dfs(i, mat, vis)

n = int(input())
ret = 0
v = 0
mat = []
vis = [False] * n 
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
    ret += sum(row)
for i in range(n):
    if not vis[i]:
        v += 1
        dfs(i, mat, vis)
print(v)
