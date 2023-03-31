def dfs_perm(L):
    if L == m:
        arrL.append(arr.copy())
        print(arr)
        return

    for i in range(len(n)):
        if v[i] != 1:
            v[i] = 1
            arr[L] = n[i]
            dfs_perm(L + 1)
            arr[L] = 0
            v[i] = 0


n = [1, 1, 1, 1, 1]
m = 3
v = [0] * len(n)
arr = [0] * m
arrL = []
dfs_perm(0)
print(arrL)
