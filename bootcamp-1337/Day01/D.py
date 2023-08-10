n = int(input())
if n < 2:
    print(1)
else:
    arr = [1, 1, 0]
    for i in range(2, n + 1):
        arr[2] = arr[1] + arr[0]
        arr[0] = arr[1]
        arr[1] = arr[2]
    print(arr[2])