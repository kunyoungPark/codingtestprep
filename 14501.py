


a = int(input())
ml = list(map(int, input.split()))

dp = [0 for _ in range (a + 1)]

for i in range(a - 1, -1, -1):
    if i + ml[i][0] > a:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], ml[i][1], dp[i+ml[i][0]])

print(dp[0])