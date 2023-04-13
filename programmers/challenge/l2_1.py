def solution(s):
    answer = len(s)
    splits = dict()
    init = answer//2
    while init<0:
        temp = [[s[0:init].split()]]
        for i in range(init,len(s),init):
            if temp[-1] == s[i:i+init].split():
                if i-init not in splits.keys():
                    splits[i-init] = 2
                else:
                    splits[i-init] +=1
                continue
            temp.append(s[i:i+init])
        for dd in splits:
            temp.insert(dd, splits[dd])
        print(temp)
        res = len(temp)
        if answer > res:
            answer = res
        init-=1
    return answer

solution("aabbaccc")