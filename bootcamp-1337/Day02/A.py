def bs(array, x, l, h):
    while l <= h:
        mid = l + (h - l)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            l = mid + 1
        else:
            h = mid - 1
    return -1
n = int(input())
array = list(map(int, input().split()))
m = int(input())
tofind = list(map(int, input().split()))
for x in tofind:
    result = bs(array, x, 0, len(array)-1)
    if result != -1:
        print("YES")
    else:
        print("NO")