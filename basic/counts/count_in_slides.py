def solution(book_time):
    answer = 0
    times = []
    for b in book_time:
        temp = list()
        for bb in b:
            time = bb.split(":")
            t = int(time[0]) * 60 + int(time[1])
            temp.append(t)
        times.append(temp)
    times.sort(key=lambda x: x[1] - x[0], reverse=True)
    print(times)

    rooms = [0] * len(book_time)
    rooms[0] = [times[0]]
    print(rooms)
    for i in range(1, len(times)):
        flag = False
        for ri in rooms:
            for rr in ri:
                if rr[1] + 10 <= times[i][0] or rr[0] >= times[i][1] + 10:
                    flag = True
                    continue
                flag = False
            if flag == True:
                ri.append(times[i])

    print(rooms)
    return answer


solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])