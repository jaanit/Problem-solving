n, q = map(int, input().split())
l = list(map(int, input().split()))
arr = [0] * (n + 1)

for i in range(1, n + 1):
    arr[i] = l[i - 1] ^ arr[i - 1]
# print(arr)
for _ in range(q):
    l, r = map(int, input().split())
    print(arr[r] ^ arr[l - 1])