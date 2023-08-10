n = int(input())
for i in range(n):
    a , b = map(int,input().split())
    print (pow(a,b,10**9 + 7))