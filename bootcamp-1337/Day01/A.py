n, q = map(int, input().split())
input_values = list(map(int, input().split()))
arr = [0] * (n + 1)
# print(arr)
for i in range(1, n + 1):
    arr[i] = input_values[i - 1] + arr[i - 1]
# print(arr)
for _ in range(q):
    l, r = map(int, input().split())
    print(arr[r] - arr[l - 1])