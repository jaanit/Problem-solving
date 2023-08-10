n = int(input())
l = []
num_list = list(int(num) for num in input().strip().split())[:n]
for i in num_list:
    if(i>=0):
        i+=2
    print(i, end=" ")