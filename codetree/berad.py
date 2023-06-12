from queue import Queue

"""
5 3
0 0 0 0 0
1 0 0 0 1
0 0 0 0 0
0 1 0 0 0
0 0 0 0 1
2 3
4 4
5 1

4 5
1 1 1 1
0 0 1 0
1 0 0 1
1 0 0 0
2 2
4 4
4 3
4 2
3 3
"""


def check_range(xx, yy):
    if xx < 0 or yy < 0 or xx >= g or yy >= g:
        return False
    if m[xx][yy] == 2:
        return False
    return True


def find_basecamp(store):
    q = Queue()
    v = [[False]*g for _ in range(g)]
    q.put(store)
    v[store[0]][store[1]] = True
    while not q.empty():
        cur = q.get()
        for ii in range(4):
            nx = cur[0] + rx[ii]
            ny = cur[1] + ry[ii]
            if check_range(nx, ny):
                if m[nx][ny] == 1 and ((nx,ny) not in basecamp):
                    return nx, ny
                if not v[nx][ny]:
                    q.put((nx, ny))
                    v[nx][ny] = True


def find_basecamp_main():
    for i in range(p):
        stores = (target[i][0] - 1, target[i][1] - 1)
        basecamp.append(find_basecamp(stores))


def find_target(p_idx, t):
    print('\n---------------', p_idx, done)
    qt = qDict[p_idx]
    cur = qt.get()
    while cur[1] == t - p_idx and done[p_idx] == 0:
        for ii in range(4):
            nx = cur[0][0] + rx[ii]
            ny = cur[0][1] + ry[ii]
            if not check_range(nx, ny):
                continue
            if (nx, ny) == (target[p_idx][0] - 1, target[p_idx][1] - 1):
                m[nx][ny] = 2
                done[p_idx] = 1
                print(basecamp[p_idx],target[p_idx],p_idx,cur[1]+p_idx+1)
                return
            if not vDict[p_idx][nx][ny]:
                qt.put([(nx,ny),cur[1]+1])
                vDict[p_idx][nx][ny] = True
        cur = qt.get()
    qt.put(cur)
    return


g, p = map(int, input().split())

m = []
for i in range(g):
    m.append(list(map(int, input().split())))

qDict = {}
vDict = {}
target = []
for i in range(p):
    target.append(tuple(map(int, input().split())))

rx = (0, -1, +1, 0)
ry = (-1, 0, 0, +1)
basecamp = []
find_basecamp_main()
#print(basecamp)

for i in range(p):
    qQ = Queue()
    qQ.put([(basecamp[i][0], basecamp[i][1] ), 1])
    qDict[i] = qQ
    vDict[i] = [[False]*g for _ in range(g)]

done=[0]*p

timer = 0
while True:
    if done.count(1) == p:
        break
    timer += 1
    m[basecamp[timer-1][0]][basecamp[timer-1][1]] = 2
    for pi in range(p):
        if done[pi] == 1:
            continue
        find_target(pi, timer)

print(timer+1)
