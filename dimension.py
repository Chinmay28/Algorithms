
x = int(input())
y = int(input())
z = int(input())
n = int(input())

outList = []
for xi in range(0, x+1):
    for yi in range(0, y+1):
        for zi in range(0, z+1):
            if xi + yi + zi == n:
                continue
            else:
                outList.append([xi, yi,zi])
                
print(outList)