import random, time

def unique_n2(A):
    s = time.process_time()
    
    for i in range(n):
	    for j in range(i+1,n):
		    if A[i] == A[j]:
			    print('No')
			    
			
			    e = time.process_time()
			    return print("수행시간 =", e-s)
		    
		    
	    
    print('Yes')
    e = time.process_time()
    return print("n^2 수행시간 =", e-s)
    

def unique_nlogn(A):
    s = time.process_time()
    print("start", s)
    quick_sort(A) #오름차순으로 정렬. => nlogn 시간?.?
    for i in range(n-1):
        if A[i] == A[i+1]:
            print('No')
            e = time.process_time()
            return print("수행시간 =", e-s)
    print('Yes')
    e = time.process_time()
    print("fin", e)
    return print("nlogn 수행시간 =", e-s)
	
def unique_n(A):
	s = time.process_time()
	B=[]
	for num in A:
		if num in B:
			print("No")
			e = time.process_time()
			return print("수행시간",e-s)
		else:
			B.append(num)
	print('Yes')
	e = time.process_time()
	return print("n 수행시간",e-s)


def quick_sort(arr):
    
    
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    
    
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

n = int(input("정수 n 입력 : "))
A = random.sample(range(-n,n+1),n)



test1 = unique_n2(A)
print()
test2 = unique_nlogn(A)

print()
test3 = unique_n(A)


