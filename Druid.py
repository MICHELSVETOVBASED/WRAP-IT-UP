n = int(input())
m = [1,1]
i = 0

while i <= n-3:
    m.append(int(m[i]+m[i+1]))
    i+=1
print(m)
