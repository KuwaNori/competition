def moveTo(d,edge_blocks,x,y,field):
    #down
    if d == 0:
        for i in range(edge_blocks-1):
            y+=1
            field[y][x] = '■'
    #left
    if d == 1:
        for i in range(edge_blocks-1):
            x-=1
            field[y][x]= '■'
    #up
    if d == 2:
        for i in range(edge_blocks-1):
            y-=1
            field[y][x] = '■'
    #right
    if d == 3:
        for i in range(edge_blocks-1):
            x+=1
            field[y][x] = '■'
    return field,x,y

def change(d):
    if d == 0: return 1
    if d == 1: return 2
    if d == 2: return 3
    else: return 0

n = 20
direction = 0
if n %2 == 0:
    fin = 2
else:
    fin = 3

field = [['□' for i in range(n)] for i in range(n)]
field[0] = ['■' for i in range(n)]

d = 0
edge_blocks = n
flag = 0
x,y = n-1,0
while edge_blocks >= fin:
    if edge_blocks == 2:
        flag = 1
    field,x,y = moveTo(d,edge_blocks,x,y,field)
    print(edge_blocks)
    print(str(x)+" : "+str(y))
    if flag == 1:
        edge_blocks-=2
        flag = 0
    else:
        flag +=1
    d = change(d)


for i in field:
    print(i)



