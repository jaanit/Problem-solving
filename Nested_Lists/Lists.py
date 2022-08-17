l = []
x= []
second_lowest_names = []
ss = set()
k = int(input())
for n in range(k):
    name = str(input())
    score = float(input())
    l.append([name, score])
    ss.add(score)
min = sorted(list(ss))[1]
for name, score in l:
     if score == min:
        x.append(name)
x = sorted(x)
for name in x:
    print(name)