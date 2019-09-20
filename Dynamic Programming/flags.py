ll = lambda:list(map(int, input().split()))
testcases = 1
# testcases = ll()
for _ in range(testcases):
    [n] = ll()
    dp = [[0,0] for i in range(n)]
    dp[0][0] = 2
    dp[0][1] = 0
    for i in range(1,n):
        if(i!=n-1):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]
        else:
            dp[i][0] = dp[i-1][0]+dp[i-1][1]
    print(dp[-1][0]) 