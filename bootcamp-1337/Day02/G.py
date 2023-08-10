def findK(arr, n, k, mid):
    count = 1
    sum = 0
    for i in range(n):
        if sum + arr[i] > mid:
            # if mid == 7 :
            #     print(count, sum, arr[i])
            count += 1
            sum = 0
        sum += arr[i]
    return count <= k
n, k = map(int, input().split())
arr = list(map(int, input().split()))
left = max(arr)
right = sum(arr)
result = right
while left <= right:
    mid = (left + right) // 2
    if findK(arr, n, k, mid):
        result = mid
        right = mid - 1
        # print(result, mid,right)
    else:
        left = mid + 1
print(result)