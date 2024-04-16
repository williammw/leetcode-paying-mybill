# %%

def climgstair(n):
  memo = {}
  def dp(n):
    if n <= 2:
      return n
    if n not in memo:
      memo[n] = dp(n-1) + dp(n-2)
    return memo[n]
  return dp(n)

print(climgstair(5)) # 8
# %%

def housRobbing(nums):
  #base case
  memo={}
  def dp(i):
    if  i == 0:
      return nums[0]
    if i == 1:
      return max(nums[0], nums[1])
    if i not in memo:
      memo[i] = max(dp(i-1), dp(i-2)+nums[i])
    return memo[i]
  return dp(len(nums)-1)

def rob(nums):
  if len(nums) == 1:
    return nums[0]
  
  dp = [0] * len(nums) # dp[i] is the max amount of money you can rob from the first i houses
  dp[0] = nums[0]
  dp[1] = max(nums[0], nums[1])
  for i in range(2, len(nums)):
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
  return dp[-1]