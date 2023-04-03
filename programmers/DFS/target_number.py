def bfs_perm():
    global cnt
    leaves = [0]
    for n in numbers:
        temp = []
        for p in leaves:
            temp.append(p + n)
            temp.append(p - n)
        leaves = temp
    cnt = leaves.count(target)
    return cnt


# sample data 1
numbers = [1, 1, 1, 1, 1]
target = 3
ans1 = 5
# sample data 2
numbers2 = [4, 1, 2, 1]
target2 = 4
ans2 = 2

nn = len(numbers)
cnt = 0
v = [0] * nn
print(bfs_perm())
