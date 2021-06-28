def find_way_from_maze(r, c):
    visited[r][c] = True
    if r == ex and c == ey : return True
    if M[r][c+1] == '0' and visited[r][c+1]==False:
        if find_way_from_maze(r,c+1)==True:
            M[r][c+1] = trace
            return True
    elif M[r+1][c] == '0' and visited[r+1][c]==False:
        if find_way_from_maze(r+1,c)==True:
            M[r+1][c] = trace
            return True
    elif M[r][c-1] == '0' and visited[r][c-1]==False:
        if find_way_from_maze(r,c-1)==True:
            M[r][c-1] = trace
            return True
    elif M[r-1][c] == '0' and visited[r-1][c]==False:
        if find_way_from_maze(r-1,c)==True:
            M[r-1][c] = trace
            return True
    else: return False




trace = '\u00B7'


n = int(input())
sx, sy, ex, ey = (int(x) for x in input().split())
M = []
# row 0 and n+1 are all 1's
# col 0 and n+1 are all 1's
for i in range(n):
    M.append([c for c in input()])

'''
n = 7
sx, sy, ex, ey = 1, 1, 5, 5
M = [['1','1','1','1','1','1','1'],['1','0','0','0','0','0','1'],['1','1','1','1','1','0','1'],['1','0','0','0','1','0','1'],['1','0','1','1','1','0','1'],['1','0','0','0','0','0','1'],['1','1','1','1','1','1','1']]
'''

visited = [[False for _ in range(n)] for _ in range(n)]
M[sx][sy] = 's'
success = find_way_from_maze(sx, sy)
print(success)
M[ex][ey] = 'e'

if success:
    for row in M:
        for c in row:
            if c == '1':
                print('#', end="")
            elif c == '0':
                print(' ', end="")
            else:
                print(c, end="")
        print()
    print()
else:
    print("NO WAY!")
