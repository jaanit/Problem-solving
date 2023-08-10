n = int(input())
arr = list(map(int, input().split()))
moves = 0
prev = arr[0]
for i in range(1, n):
    if arr[i] < prev:
        moves += prev - arr[i]
    else:
        prev = arr[i]
print(moves)