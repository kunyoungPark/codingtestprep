from queue import Queue


def simulation(data, startx, starty, cur_dir, maxx, maxy):
    rx = (0, +1, 0, 1)
    ry = (-1, 0, + 1, 0)

    s = (startx, starty)
    q = Queue()
    d = dict()
    d[s] = -1
    q.put(s)
    cnt = 1
    while q.qsize() > 0:
        cur = q.get()
        for i in range(4):
            cur_dir = 4 % (cur_dir + 3)
            curx = cur[0] + rx[cur_dir]
            cury = cur[1] + ry[cur_dir]
            new_cur = (curx, cury)
            if curx < 0 or cury < 0 or curx > maxx - 1 or cury > maxy - 1:
                continue
            if cur not in d or data[curx][cury] != 1:
                d[new_cur] = cur
                q.put(new_cur)
                cnt += 1
    print(len(d))
    print(cnt)
    return cnt


maxx, maxy = map(int, input().split())
startx, starty, cur_dir = map(int, input().split())
data = list()
for mx in range(maxx):
    data.append(list(map(int, input().split())))
simulation(data, startx, starty, cur_dir, maxx, maxy)
