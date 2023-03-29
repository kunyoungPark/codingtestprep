
# 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다.
# (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데,
# 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.



a = int(input())

nums = list(map(int, input().split()))
add, diff, mul, div = map(int, input.split())

def dfs(idx, add, diff, mul, div, res):
     global  ans_max, ans_min
     if idx == len(nums):
         ans_max = max(ans_max, res)
         ans_min = min(ans_min, res)
         return

     if add > 0:
         dfs(add - 1, diff, mul, div, res+nums[idx], idx+1)
     if diff > 0:
         dfs(add, diff - 1, mul, div, res - nums[idx], idx + 1)
     if mul > 0:
         dfs(add, diff, mul - 1, div, res * nums[idx], idx + 1)
     if div > 0:
         dfs(add, diff, mul, div - 1, int(res / nums[idx]), idx + 1)


dfs(add, diff, mul, div, nums[0], 1)
print(ans_max)
print(ans_min)
