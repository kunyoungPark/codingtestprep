

def DFS(dataDict, cur):

    if cur == -1:
        return

    dataDict[cur]["v"] = True
    print(cur)

    cntN = 0
    for n in dataDict[cur]["NN"]:
        if not dataDict[n]["v"]:
            cntN += 1
            dataDict[n]["par"] = cur
            DFS(dataDict, n)

    if cntN == 0:
        DFS(dataDict, dataDict[cur]["par"])


data_ll = {1: [2, 3], 2: [1, 4, 5], 3: [1, 4, 6], 4: [2, 3, 5, 6, 7], 5: [2, 4, 7, 8], 6: [3, 4, 7, 9],
           7: [4, 5, 6, 10], 8: [5, 10], 9: [6, 10], 10: [7, 8, 9]}
# data structuring
d = dict()
for dl in data_ll:
    d[dl] = {"NN": data_ll[dl], "v": False, "par": -1}

DFS(d, 1)
