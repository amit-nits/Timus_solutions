ll = lambda:list(map(int, input().split()))
testcases = 1
for _ in range(testcases):
	[n,m] = ll()
	mat = [[0 for i in range(m)] for i in range(n)]
	k = int(input())
	dp = [[0 for i in range(m+1)] for i in range(n+1)]
	for i in range(k):
		[x,y] = ll()
		mat[x-1][y-1] = 1
	x = 1.4142
	dp[0][0] = 0
	for i in range(n+1):
		dp[i][0] = i
	for i in range(m+1):
		dp[0][i] = i
	for i in range(1,n+1):
		for j in range(1,m+1):
			dp[i][j] = min(dp[i][j-1], dp[i-1][j])+1
			if(mat[i-1][j-1]==1):
				dp[i][j] = min(dp[i-1][j-1]+x,dp[i][j])
	# print(dp)
	print(round(dp[-1][-1]*100))

