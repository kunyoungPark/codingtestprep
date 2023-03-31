

def bfs_perm(L):
    global cnt
    if L == n1:
        if operate(n, opArr) == target:
            cnt += 1
        return

    for 

def operate(n, o):
    ans = n[0]
    for i in range(1,n):
        #0 => + 1=> -
        if o[i-1] == 0:
            ans += n[i]
        else:
            ans -= n[i]
    return ans

#sample data 1
numbers = [1, 1, 1, 1, 1]
target = 3
ans1 = 5
#sample data 2
numbers2 = [4, 1, 2, 1]
target2 = 4
ans2 = 2

n1 = len(numbers) - 1
os = [0] * len(numbers)
cnt = 0