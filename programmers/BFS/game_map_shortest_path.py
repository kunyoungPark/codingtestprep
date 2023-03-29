from queue import Queue
import time


def dfs(data):
    # directions
    tx = (+1, -1, 0, 0)
    ty = (0, 0, +1, -1)

    # start
    sp = (0, 0)
    ep = (len(data)-1, len(data[0])-1)

    # data dict
    d = dict()
    q = Queue()
    q.put(sp)
    d[sp] = -1
    while q.qsize() > 0:
        cur = q.get()
        for i in range(4):
            x = cur[0] + tx[i]
            y = cur[1] + ty[i]
            new_cur = (x, y)
            if x < 0 or y < 0 or x > ep[0] or y > ep[0]:
                continue
            if new_cur == ep:
                d[new_cur] = cur
                return len(find_path(d, new_cur))
            if (new_cur not in d) and data[x][y] != 0:
                q.put(new_cur)
                d[new_cur] = cur
    return -1

def find_path(d, new_cur):
    path = list()
    path.append(new_cur)
    par = d[new_cur]
    while par != -1:
        path.append(par)
        par = d[par]
    return path


# sample data
data1 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
"""
[1,0,1,1,1]
[1,0,1,0,1]
[1,0,1,1,1]
[1,1,1,0,1]
[0,0,0,0,1]
"""
data2 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(dfs(data1))
print(dfs(data2))
