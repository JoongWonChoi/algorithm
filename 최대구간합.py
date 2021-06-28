A = input().split()
A = [int(x) for x in A]
k = len(A)
result = []
for i in range(0,k):# 리스트 인덱스의 요소 i들에 대하여 값 구하기
    max_r = 0
    sum_r = 0
    max_l = 0
    sum_l = 0
    _max_ = 0
    if i==0: #첫 인덱스를 포함하는 경우(좌측 인덱스가 없다. 우측 인덱스들만 고려)
        max_r = A[1]
        sum_r = A[1]
        for j in range(2,k):
            sum_r+=A[j] #현재 합의 값에 다음 인덱스 더하기
            if max_r < sum_r: #현재 연속구간 합 최대값과(max_r) 다음 인덱스를 더한 값 비교(sum_r)
                max_r = sum_r
        _max_ = max(max_r+A[i],A[i])
        result.append(_max_)

    elif i > 0 and i < k - 1:
        max_l = A[i]
        sum_l = A[i]
        for j in range(i-1,-1,-1):
            sum_l += A[j]
            if max_l<sum_l:
                max_l = sum_l
        max_l = max(max_l,A[i])

        max_r = A[i]
        sum_r = A[i]
        for l in range(i+1,k):
            sum_r += A[l]
            if max_r < sum_r:
                max_r = sum_r
        max_r = max(max_r,A[i])
        _max_ = max_r + max_l - A[i]
        result.append(_max_)

    elif i==k-1: # i가 마지막 인덱스, 왼쪽(작은) 인덱스들만 고려
        max_l = A[i-1]
        sum_l = A[i-1]
        for j in range(i-2,-1,-1):
            sum_l += A[j]
            if max_l < sum_l:
                max_l = sum_l
        _max_ = max(max_l+A[i],A[i])
        result.append(_max_)


print(result)


