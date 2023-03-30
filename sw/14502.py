from queue import Queue
def virus_BFS():
    rx = [+1, -1, 0, 0]
    ry = [0, 0, +1, -1]
    q = Queue()
    mapde = mapd.copy()
    print(mapde)
    for mi in range(n):
        for mj in range(m):
            if mapde[mi][mj] == 2:
                q.put((mi,mj))

    while q.qsize() > 0:
        cur = q.get()
        for i in range(4):
            cx = cur[0] + rx[i]
            cy = cur[1] + ry[i]
            if cx > n-1 or cy > m-1 or cx < 0 or cy < 0 :
                continue
            if mapde[cx][cy] == 0:
                print(mapde[cx][cy])
                q.put((cx, cy))
                mapde[cx][cy] = 2
    cnt = 0

    for i in range(n):
        cnt += mapde[i].count(0)
    global answer
    answer = max(answer, cnt)


def wall_rec(cnt):
    if cnt == 3:
        virus_BFS()
        return

    for i in range(n):
        for j in range(m):
            if mapd[i][j] == 0:
                mapd[i][j] = 1
                wall_rec(cnt + 1)
                mapd[i][j] = 0


n, m = map(int, input().split())
mapd = []

for i in range(n):
    mapd.append(list(map(int, input().split())))

answer = 0
wall_rec(0)
print(answer)