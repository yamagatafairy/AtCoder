import io
import sys

_INPUT = """\
6
30 10 60 10 60 50
"""
sys.stdin = io.StringIO(_INPUT)

#本文開始
N = int(input())
H = list(map(int, input().split()))

# [cost][position]
# start Data
dp = [0] * len(H)

dp[0] = 0
dp[1] = dp[0] + abs(H[0] - H[1])

for i in range(N-2):
    plus1 = abs(H[i] - H[i+2]) + dp[i]
    plus2 = abs(H[i+1]- H[i+2]) + dp[i+1]
    #print(f"plus1:{plus1} plus2:{plus2}")
    dp[i+2] = min(plus1, plus2)

#print(dp)
print(dp[N-1])
