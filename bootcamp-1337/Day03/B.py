n = int(input())

for _ in range(n):
    str_input = input()
    res = 1

    for i in range(len(str_input)):
        if i == 0 and str_input[i] == '0':
            res = 0
            break
        elif i == 0 and str_input[i] == '?':
            res = res * 9
        elif str_input[i] == '?':
            res *= 10

    print(res)
n = int(input())

for _ in range(n):
    str_input = input()
    res = 1

    for i in range(len(str_input)):
        if i == 0 and str_input[i] == '0':
            res = 0
            break
        elif i == 0 and str_input[i] == '?':
            res = res * 9
        elif str_input[i] == '?':
            res *= 10

    print(res)