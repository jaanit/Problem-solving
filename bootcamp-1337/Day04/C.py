def solve(adj_matrix):
    n = len(adj_matrix)
    src = []
    sinks = []
    for i in range(n):
        if sum(adj_matrix[i]) == 0:
            src.append(i + 1) 

        if sum(row[i] for row in adj_matrix) == 0:
            sinks.append(i + 1)
    return src, sinks
n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)
src, sinks = solve(adj_matrix)
print(len(sinks), *sinks)
print(len(src), *src)
