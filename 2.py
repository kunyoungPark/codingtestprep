import math
def solution(brown, yellow):
    answer = []
    i1 = math.floor(math.sqrt(brown+yellow))
    i2 = (brown+yellow)//i1
    return sorted([i2,i1], reverse=True)

print(solution(50,50))