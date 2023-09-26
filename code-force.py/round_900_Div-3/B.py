t = int(input())
for _ in range(t):
    n = int(input())
    l = 2
    r = 4
    i =5
    j = 0
    while j<n:
        # if ((3*i) % (l + r)):
        print(i,end="")
        print(" ",end="")
        j+=1
        l = r
        r = i
        i+=1
