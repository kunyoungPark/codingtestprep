
def dfs_maxp(L):
    global sumDays, pay, maxpay
    if L == n or sumDays >= n:
        print(pay)
        if maxpay < pay:
            maxpay = pay
        sumDays = 0
        pay = 0
        return

    for i in range(n):
        if not d[i]["v"]:
            d[i]["v"] = True
            sumDays += d[i]["days"]
            pay += d[i]["p"]
            dfs_maxp(L + 1)
            d[i]["v"] = False


n = int(input())
d = dict()
for i in range(n):
    temp = list(map(int, input().split()))
    d[i] = {"days": temp[0], "v": False, "p": temp[1]}

sumDays = 0
pay = 0
maxpay = 0
dfs_maxp(0)
print(sumDays, pay, maxpay)