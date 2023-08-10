nb_of_machine , nb_of_product = map(int, input().split())
machine = list(map(int, input().split()))
low = 0
high = max(machine) * nb_of_product
res = 0
mid = low + (high - low) // 2
while(low <= high):
    mid = low + (high - low) // 2
    total = 0
    for i in range(nb_of_machine):
        total += (mid // machine[i])
        if total >= nb_of_product:
            break
    if total >= nb_of_product:
        high = mid - 1
        res = mid
    else:
        low = mid + 1
print(int(low))