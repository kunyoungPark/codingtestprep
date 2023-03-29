import networkx as nx
from queue import Queue
import time


class node:
    def __init__(self, idx):
        self.nn = list()
        self.visit = False
        self.discovered = False
        self.cnt_child = len(self.nn)
        self.par = -1
        self.idx = idx


def bfs_ll_class(data, start, end):
    time1 = time.time()
    datalist = list()
    # generate objects
    for d in data:
        temp = node(d)
        temp.nn = data[d]
        datalist.append(temp)
    time2 = time.time()
    # bfs
    start = datalist[start - 1]
    start.visit = True
    q = Queue()
    q.put(start)
    while q.qsize() > 0:
        cur = q.get()
        cur.visit = True
        for i in cur.nn:
            if datalist[i - 1].idx == end:
                break
            if datalist[i - 1].visit != True and datalist[i - 1].discovered != True:
                q.put(datalist[i - 1])
                datalist[i - 1].discovered = True
    time3 = time.time()
    print(time2 - time1, time3 - time2)

def bfs_ll_dict(data, start, end):
    time1 = time.time()
    datalist = dict()
    # generate objects
    for d in data:
       datalist[d] = {"idx": d, "visited": False, "discovered": False, "nn": data[d]}
    time2 = time.time()
    # bfs
    start = datalist[start]
    start["visited"] = True
    q = Queue()
    q.put(start)
    while q.qsize() > 0:
        cur = q.get()
        cur["visited"] = True
        for i in cur["nn"]:
            new_cur = datalist[i]
            if new_cur["idx"] == end:
                break
            if new_cur["visited"] != True and new_cur["discovered"] != True:
                q.put(new_cur)
                new_cur["discovered"] = True
    time3 = time.time()
    print(time2 - time1, time3 - time2)

def bfs_sp_ll_class(data, start, end):
    time1 = time.time()
    datalist = list()
    # generate objects
    for d in data:
        temp = node(d)
        temp.nn = data[d]
        datalist.append(temp)
    # bfs
    start = datalist[start - 1]
    start.visit = True
    q = Queue()
    q.put(start)
    while q.qsize() > 0:
        cur = q.get()
        cur.visit = True
        for i in cur.nn:
            if datalist[i - 1].idx == end:
                time2 = time.time()
                print(time2-time1)
                return find_path_ll_class(cur, datalist, end)
            if datalist[i - 1].visit != True and datalist[i - 1].discovered != True:
                q.put(datalist[i - 1])
                datalist[i - 1].discovered = True
                datalist[i - 1].par = cur

def find_path_ll_class(cur, datalist, end):
    path = list()
    path.append(cur.idx)
    while cur.par != -1:
        cur = datalist[cur.idx - 1].par
        path.insert(0, cur.idx)
    path.append(end)
    return path


def bfs_sp_ll_dict(data, start, end):
    time1 = time.time()
    datalist = dict()
    # generate objects
    for d in data:
       datalist[d] = {"idx": d, "visited": False, "discovered": False, "nn": data[d], "par": -1}
    # bfs
    start = datalist[start]
    start["visited"] = True
    q = Queue()
    q.put(start)
    while q.qsize() > 0:
        cur = q.get()
        cur["visited"] = True
        for i in cur["nn"]:
            new_cur = datalist[i]
            if new_cur["idx"] == end:
                time2 = time.time()
                print(time2-time1)
                return find_path_ll_dict(cur, datalist, end)
            if new_cur["visited"] != True and new_cur["discovered"] != True:
                q.put(new_cur)
                new_cur["discovered"] = True
                new_cur["par"] = cur


def find_path_ll_dict(cur, datalist, end):
    path = list()
    path.append(cur["idx"])
    while cur["par"] != -1:
        cur = datalist[cur["idx"]]["par"]
        path.insert(0, cur["idx"])
    path.append(end)
    return path




# linear list
data_ll = {1: [2, 3], 2: [1, 4, 5], 3: [1, 4, 6], 4: [2, 3, 5, 6, 7], 5: [2, 4, 7, 8], 6: [3, 4, 7, 9],
           7: [4, 5, 6, 10], 8: [5, 10], 9: [6, 10], 10: [7, 8, 9]}

# adj matrix
data_mat = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]

"""
g1 = nx.Graph()
g2 = nx.Graph()

g1.add_nodes_from(list(data_ll.keys()))
g2.add_nodes_from([i for i in range(10)])

for d in data_ll:
    for a in data_ll[d]:
        g1.add_edge(d, a)
# nx.draw(g1)

for i in range(10):
    for j in range(10):
        if data_mat[i][j] == 1:
            g2.add_edge(i, j)
nx.draw(g2)
"""

print(bfs_sp_ll_class(data_ll, 1, 10))

print(bfs_sp_ll_dict(data_ll, 1, 10))
