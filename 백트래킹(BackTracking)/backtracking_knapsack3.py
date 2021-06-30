def knapsack(i, size, mp):
    if i>=n or size<=0:
        return mp #전 level로 복귀.
    sv, pv,maxprofit  = 0, 0, 0
    for j in range(n):
        if x[j]==1:
            sv += s[j]
            pv += p[j]
    #x[i]==1
    if s[i]<=size:
        B = frac(i+1,size-s[i])
        if mp<pv+p[i]+B:
            x[i] = 1
            mp = max(mp,pv+p[i])
            maxprofit = mp
            print(x)
            knapsack(i+1,size-s[i], mp)
            x[i] = None

    #x[i]==0
    B = frac(i+1,size)
    if maxprofit<pv+B:
        x[i]=0
        print(x)
        print()
        knapsack(i+1,size, maxprofit)
        x[i] = None

    return mp




def frac(i,size):
    ep = 0
    while i<n and size>0:
        if size>=s[i]:
            ep += p[i]
            size -= s[i]
            i+=1
        else :
            ep += size * (p[i]/s[i])
            break
    return ep
k = 16
n = 4
i = 0
x = [None]*n
s = [2, 5, 10, 5]
p = [40, 30, 50, 10]

mp = 0
print(knapsack(i,k, mp))