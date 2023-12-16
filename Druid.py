x = int(input())
l = []
for i in range(x):
    row =[]
    for j in range(x):
        if j == x-1:
            row.append(5)
        else : 
            row.append(1)
    l.append(row)
for row in l:
    print(*row)