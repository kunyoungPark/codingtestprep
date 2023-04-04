from queue import Queue


def bfs():
    for i in range(p):
        pass


def nn(cord):
    q = Queue()
    q.put(cord)
    d = dict()
    d[cord] = {"v": True}
    while q.empty == False:
        cur = q.pop()
        for idx in range(4):
            new_curx = cur[0] + rx[i]
            new_cury = cur[1] + ry[i])
            if

            g, p = map(int, input().split())

            m =[]
            for i in range(g):
                m.append(list(map(int, input().split())))

            target = []
            for i in range(p):
                target.append(tuple(map(int, input.split())))

            rx = (0, -1, +1, 0)
            ry = (1, 0, 0, -1)