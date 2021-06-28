def knapsack(size, i):  # size = 남은 용량
    if i >= n or size <= 0:
        print("i = %d" % i, ", x=", x)
        print("i or size reached last, backtrack before level.\n")
        return   # i : index for test, size : left bag size
    # p(v), s(v) calculate ;; before i_th sum of profit and size
    print("just print x", x)

    pv = 0
    sv = 0
    for j in range(n):
        if x[j]==1:
            pv+=item_profit[j]
            sv+=item_size[j]
    print("pv,sv", pv, sv)
    # if x[i]=1 // if i_th item put in bag
    if item_size[i] <= size:  # 남은 bag공간보다 들어올 item의 크기가 작아야함. 크면 0/1방식이기 때문에 접근 불가.
        print("%d th round (put in bag)" % (i + 1))
        B = frac(i + 1, size - item_size[i])  # select i_th item => size down
        if pv + item_profit[i] + B > mp:
            print("Expect mp : %d, current mp : %d" % (pv + item_profit[i] + B, mp))
            x[i] = 1
            print("x[%d] = 1" % i)
            mp = max(mp, pv + item_profit[i])
            print("======mp =======: ", mp)
            print("go to next level\n")
            knapsack(size - item_size[i], i + 1)
        else:
            print("backtrack! no need to search")
            return   # if before mp > current mp => no reason for search
    print("over the size")
    print("x = ", x)
    print("mp : ", mp)
    print()
    # if x[i]=0 // if i_th item not put in bag
    x[i] = 0
    print("%d th round (not in bag)" % (i + 1))
    print("x[%d] = 0" % i)

    B = frac(i + 1, size)  # no select i_th item => no change size
    if pv + B > mp:  # no choose curretn i_th item => dont need to add itemp[i]
        # mp = max(mp, p_v + item_profit[i]) x[i] = 0이면 해당 level에선 pv,sv,mp 전 레벨과 동일.
        print("-----mp------: ", mp)
        knapsack(size, i + 1)
    else:
        print("backtrack! no need to search(..) mp =", mp)
        print()
        return   ##if before mp > current mp => no reason for search


def frac(i, size):  # i+1 ~ n get fractional max profit
    print("enter frac")
    print("left bag size : %d" % size)
    ep = 0
    while size > 0 and i < n:
        if item_size[i] <= size:
            ep += item_profit[i]
            size -= item_size[i]
            i += 1
        else:
            ep = ep + (size * (item_profit[i] / item_size[i]))
            print("frac_bag full")
            break
    print("expect max profit ", ep)
    return ep


'''
k = int(input("k")) #bag size
n = int(input("n"))
item_size = [int(x) for x in input("size").split()] # item size (list)
item_profit = [int(y) for y in input("profit").split()] #  item profit (list)
item_ef = [] # item efficient
profit_ef = []

for l in range(n):
    efficient = item_profit[l]/item_size[l]
    item_ef.append(efficient)
    profit_ef.append([item_profit[l],efficient])

profit_ef.sort(reverse = True,key=lambda x: x[1])
i = 0 # index num
mp = 0 # MaxProfit
x = []
p_v = 0 # profit sum before i_th index
s_v = 0 # size sum before i_th index
'''

k = 16
i = 0
mp = 0
n = 4
x = [None] * n
item_size = [2, 5, 10, 5]
item_profit = [40, 30, 50, 10]
print("result", knapsack(k, i))

















