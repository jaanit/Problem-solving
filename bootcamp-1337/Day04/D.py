def solve():
    n = int(input())
    q = int(input())
    vec = [[] for _ in range(n)]
    
    for _ in range(q):
        k = int(input())
        if k == 1:
            a, b = map(int, input().split())
            vec[a - 1].append(b - 1)
            vec[b - 1].append(a - 1)
        else:
            a = int(input())
            for w in vec[a - 1]:
                print(w + 1, end=" ")
            print()

if __name__ == "__main__":
    solve()
