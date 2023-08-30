t = int(input())
out =0
for _ in range(t):
    n,a,q =(map(int,input().split()))
    s = input()
    online  = s.count('+') + a
    on = a
    for i in s:
        if (on >= n):
            break
        if (i == '+'):
            on += 1
        if (i == '-'):
            on -= 1
    
    if on >= n:
        print('YES')
    elif online < n:
        print('NO')
    else:
        print('MAYBE')







