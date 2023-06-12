def solution(n):
    data = []
    answer = []
    for i in range(n):
        data.append([0] * (i + 1))
    flag = [(+1, 0), (0, +1), (-1, -1)]
    iter = 0
    lim = 1
    cur = (-1, 0)
    while iter < n+1:
        dir = flag[iter % 3]
        for i in range(n - iter):
            cur = (cur[0] + dir[0], cur[1] + dir[1])
            data[cur[0]][cur[1]] = lim
            lim += 1
        iter += 1
    for i in range(n):
        answer += data[i][0:]
    return answer

print(solution(7))

