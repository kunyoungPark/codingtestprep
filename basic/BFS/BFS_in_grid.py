from queue import Queue
import time


def dfs(data):
    #directions
    tx = (+1, -1, 0, 0)
    ty = (0, 0, +1, -1)

    #start
    sp = (0,0)
    ep = (len(data[0]), len(data[0]))

    #data dict
    d = dict()
    q = Queue()
    q.put(sp)
    d[sp] = -1
    while q.qsize() > 0:
        cur = q.get()
        print(cur)
        for i in range(4):
            x = cur[0] + tx[i]
            y = cur[1] + ty[i]
            new_cur = (x,y)
            if x < 0 or y < 0:
                continue
            if new_cur == ep:
                print(new_cur)
                return
            if (new_cur not in d) :
                q.put(new_cur)
                d[new_cur] = cur


#sample data
data1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
"""
[1,0,1,1,1]
[1,0,1,0,1]
[1,0,1,1,1]
[1,1,1,0,1]
[0,0,0,0,1]
"""


dfs(data1)