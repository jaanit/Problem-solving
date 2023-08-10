n = int(input())
for _ in range(n):
    s = input()
    stack = []
    mp = {')': '(', ']': '['}
    for c in s:
        if stack and c in mp.keys() and stack[-1] == mp[c]:
            stack.pop()
            continue
        stack.append(c)
    print("Yes" if not stack else "No")