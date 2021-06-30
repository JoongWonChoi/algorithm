A = input().split()
A = [int(x) for x in A]
for i in range (len(A)):
    s=[0]*len(A)
    s[0] = A[i]
    #s 는 dynamic programming을 사용하여 A[i]까지 구간의 합의 최대값을 저장하는 용도
     #동적프로그래밍을 위한 초기 값 설정. A[0]까지의 합은 A[0] 이다.
    for k in range (1,len(A)-i):
        s[k] = max(s[k-1]+A[k+i],A[k+i]) #S[1]부터의 값은 A[0]+A[1]+..처럼 더하면서 나아가야함. 그런데 인덱스중 음수가 있을 수 있으니 A리스트 값과 비교를 해야함.
    _max1_ = max(s)
    s = [0] * len(A)
    s[i] = A[i]
    for j in range(i-1,-1,-1):
        s[j] = max(s[j+1]+A[j],A[j])
    _max2_ = max(s)
    _max_ = _max1_+_max2_- A[i]
    print(_max_, end=' ')



'''
for i in range(len(A)):
    prefix_l=[]
    prefix_r=[]
    sum_l, sum_r, _max_l, _max_r, _max_ = 0, 0, 0, 0, 0
    for j in range(i,-1,-1):
        sum_l+=A[j]
        prefix_l.append(sum_l)
    _max_l = max(prefix_l)
    for k in range(i,len(A)):
        sum_r+=A[k]
        prefix_r.append(sum_r)
    _max_r = max(prefix_r)
    _max_ = _max_r + _max_l - A[i]
    print(_max_,end=' ')
'''



