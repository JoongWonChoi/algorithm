def pin(A):

    '''
    i=1
    while i<len(A):
        print("before exec ;len(A) =>",len(A))
        if(A[i][0]<=A[i-1][1] and A[i-1][1]<=A[i][1]):
            A.pop(i)
            i+=1
        else:
            pin+=1
            i+=1
        print("after exec ;len(A) =>", len(A))
        print("i => ",i)

    print(A)
    pin = 1
    current = 0
    A.sort(key=lambda x:x[1])
    for i in range(1,len(A)):
        if(A[i][0]<=A[current][1] and A[current][1]<=A[i][1]):
            print("%d stick is in current stick"%i)
        else:
            print("%d stick in not in current stick. pin + 1"%i)
            pin+=1
    '''
    '''
    A.sort(key=lambda x: x[1])
    print(A)
    pin = 1
    current = 0
    i = 1
    while(current<len(A)):
        print()
        print(A[i])
        print()
        if i==len(A)-1 :
            print("search fin")
            break
        if (A[i][0] <= A[current][1] and A[current][1] <= A[i][1]):
            print("this i is in standard ,, ",A[i])
            print("%d stick is in current stick" % i)
            i+=1 #현재 막대에 포함되는 막대가 있으면 그 다음 막대 탐색
        else:# 포함되지 않으면
            print(A[i])
            print("%d stick is not in current stick. pin + 1" % i)
            pin += 1 #포함되지 않으면 다음 current막대로 넘어가야 하기 때문에 pin+1.
            current = i #비교대상이 된 막대로 이동!(비교대상이 된 막대부터 포함되지 않았기 때문에 그 막대부터 새로 비교를 해야함.
            i = current + 1
            if i >= len(A) - 1:
                print("fininsh searching")
                break

        print("current = %d, i = %d, pin = %d"%(current,i,pin))
    return pin
    '''
    print(A)

    current = 0 # 기준 막대 인덱스
    i = 1 # 비교대상 막대 인덱스
    pin = 0
    poplist = [0]
    while len(A)>0:
        if i == len(A): # 비교대상 막대 인덱스가 마지막까지 가면 poplist에 쌓여있던 막대 인덱스들 pop하기.
            print("pop list 작성 완료", poplist)
            for k in poplist:
                A[k] = -1
            print(A)
            for j in range(len(A)):
                if -1 in A:
                    A.remove(-1)

            print()
            print("after pop.. list A",A)
            print()
            pin+=1 #pop리스트에 요소가 몇개였던 pin은 한개 추가해주면 됨.
            print("pin ==> ",pin)
            poplist = [0] # pop과정이 마치면 다시 리스트를 초기화
            i = 1         # 마찬가지로 비교대상 인덱스 i 초기화
        if len(A)==0 : return pin
        if len(A) == 1: #pop 과정들을 마치고 리스트에 요소 하나가 남은 경우 => pin 이 추가로 한개가 더 필요하다. 따라서 pin을 추가해주고 return.
            pin+=1
            return pin
        print("A[current] ==> ", A[current])
        print("A[i] ==> ",A[i])
        print()
        print("tmpA => ",A)
        if(A[i][0] <= A[current][1] and A[current][1] <= A[i][1]):#겹치는 막대 있으면 poplist에 추가, 비교대상 인덱스 i++하며 다음 막대와 비교.\
            poplist.append(i)
            print("append한 i ===> %d"%i)
            i+=1
            print("겹침")
            print("i => %d" % i)
            print()
        else :
            i+=1 #겹치지 않았다면 그냥 비교대상 막대 인덱스 +1.
            print("안겹침")
            print("i => %d" % i)
            print()
        ## i ~ n-1 까지 거친 후 pop과정을 마치면 새롭게 리스트 A 가 완성됨. 이 과정을 len(A)==0 일 때 까지 반복.
    return pin











'''
n = int(input("정수 입력"))
A=[]
for i in range(n):
    a = input().split()
    A.append([int(x) for x in a])
print(pin(A))
'''
A = [[7,7],[3,4],[0,10],[2,5],[3,5]]
B = [[19,19],[1,11],[19,20],[16,17],[2,11],[2,2],[18,18],[3,16],[1,11],[8,8]]
#(print(pin(A))
print(pin(B))


