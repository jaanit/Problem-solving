n = int(input())
print(n,sep='',end=":")
i = 2
while (i * i <= n):
    while n%i==0:
        print(" ",i,sep='',end="")
        n=n//i
    i += 1
if n>1:
    print(" ",n,sep='',end="")
print()