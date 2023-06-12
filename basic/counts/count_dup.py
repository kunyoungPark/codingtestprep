
def countDup(lista):
    idx = 0
    temp = list()
    while idx < len(lista)-2:
        cur = lista[idx]
        nxt = lista[idx+1]
        cnt = 1
        while cur == nxt  and idx < len(lista)-2:
            cnt += 1
            idx +=1
            cur = lista[idx]
            nxt = lista[idx + 1]
        temp.append([cnt, cur])
        print(temp)
        idx += 1
    answer = 0
    for t in temp:
        if t[0] != 1:
            answer+=1+len(t[1])
        else:
            answer+=len(t[1])
    return answer

def countDup_increaseby(lista, init):
    idx = 0
    temp = list()
    while idx < len(lista)-1-init:
        cur = lista[idx:idx+init]
        nxt = lista[idx+init:idx+init+init]
        cnt = 1
        while cur == nxt  and idx < len(lista)-1-init:
            cnt += 1
            idx +=init
            cur = lista[idx:idx + init]
            nxt = lista[idx + init:idx + init + init]
        temp.append([cnt, cur])
        print(temp)
        idx += 1
    answer = 0
    for t in temp:
        if t[0] != 1:
            answer+=1+len(t[1])
        else:
            answer+=len(t[1])
    answer += init -1
    return answer

countDup(['a','a','b','b','a','c','c','c'])
countDup_increaseby(['a','a','b','a','a','b','c','c'],3)