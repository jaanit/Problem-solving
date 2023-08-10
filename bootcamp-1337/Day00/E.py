import re
tab = set()
while True:
    try:
        l = list(i for i in input().split())
        if (l[0] == "insert"):
            ((tab.add(l[1])))
        elif ( l[0] == "delete" and l[1] in tab):
            tab.remove(l[1])
        elif (l[0] == "exists"):
            if (l[1] in tab):
                print("true")
            else:
                print("false")
    except:
        break