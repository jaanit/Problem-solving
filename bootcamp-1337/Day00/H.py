import heapq

nq = list(map(int, input().split()))
n = nq[0]
q = nq[1]
queues = [[] for _ in range(n)]
for _ in range(q):
    query = list(map(int, input().split()))
    t = query[0]
    if t == 0:
        i, x = query[1], query[2]
        heapq.heappush(queues[i], -x) 
    elif t == 1:
        i = query[1]
        if queues[i]:
            print(-queues[i][0]) 
    elif t == 2:
        i = query[1]
        if queues[i]:
            heapq.heappop(queues[i])