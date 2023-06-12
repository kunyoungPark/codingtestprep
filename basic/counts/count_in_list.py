def solution(want, number, discount):
    answer = 0
    dd = dict()
    for i in range(len(want)):
        dd[want[i]] = number[i]
    print(dd)
    idx = 0
    while idx + 10 < len(discount):
        cur = discount[idx:idx + 10]
        if len(set(cur)) < len(set(want)) :
            continue
        c = True
        for w in want:
            print(w, cur.count(w),dd[w])
            if cur.count(w) != dd[w]:
                c = False
                break
        if c:
            answer = idx
            print(answer)
        idx += 1

    return answer


solution(	["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])