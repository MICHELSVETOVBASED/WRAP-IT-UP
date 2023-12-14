n = input()
summ = []
for i in range(0,len(n)):
    if n[i] == 'р' and n[i+1] == 'а':
        summ.append(i)
if len(summ) > 0 :
    print(*summ)
else : print(-1)