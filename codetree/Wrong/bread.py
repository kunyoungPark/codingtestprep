from queue import Queue


def main():
    realMax = 0
    maxDist = 0
    for i in range(p):
        cur = bfs_nn((target[i][0]-1,target[i][1]-1), i)
        maxDist = max(maxDist, cur)
        if cur == maxDist:
            realMax = maxDist + i
    return realMax

def bfs_nn(cord, p_idx):
    q = Queue()
    q.put([cord, 1])
    while not q.empty():
        cur = q.get()
        dist = cur[1] + 1
        if dist in d:
            for ii in d[dist]:
                m[ii[0]][ii[1]] = 2
        for idx in range(4):
            new_curx = cur[0][0] + rx[idx]
            new_cury = cur[0][1] + ry[idx]
            if new_cury >= g or new_curx >= g or new_curx < 0 or new_cury < 0:
                continue
            if m[new_curx][new_cury] == 1:
                m[new_curx][new_cury] = 2
                d[p_idx+1] = [(new_curx, new_cury)]
                d[dist+1] = [cord]
                return dist
            if m[new_curx][new_cury] == 0:
                q.put([(new_curx, new_cury), dist])


g, p = map(int, input().split())

m = []
for i in range(g):
    m.append(list(map(int, input().split())))

target = []
for i in range(p):
    target.append(tuple(map(int, input().split())))

rx = (0, -1, +1, 0)
ry = (-1, 0, 0, +1)
d = dict()




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
"""