def gr_class(S,F):
    L = [0]
    result = 1
    current_class = 0
    for i in range(1,len(S)):
        if F[current_class]<=S[i]:
            current_class = i
            L.append(i)
            result += 1
    return result , L







start = [1,3,0,5,3,5,6,8,8,2,12]
fin = [4,5,6,7,8,9,10,11,12,13]
print(gr_class(start,fin))