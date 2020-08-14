grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

leftRight = []
for i in range(len(grid)):
    max = -1
    for j in range(len(grid[0])):
        if grid[i][j]>= max:
            max = grid[i][j]
        #duyệt từ trái sang phải từ trên xuống dưới
        print(grid[i][j],end=' ')
    leftRight.append(max)
    print()

print("-----------")
topBottom = []
for i in range(len(grid)):
    max = -1
    for j in range(len(grid[0])):
        if grid[i][j]>= max:
            max = grid[j][i]
        #duyệt từ trên xún dưới từ trái sang phải
        print(grid[j][i],end=' ')
    topBottom.append(max)
    print()
print('---------')
print(leftRight)
print(topBottom)
