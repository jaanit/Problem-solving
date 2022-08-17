if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x = []
    re = 0
    for i , j in student_marks.items():
        if i == query_name:
            x.append(j)
    for s in x:
        for k in s:
            re += k
        print("%.2f" % float(re/len(s)))
