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

# %%

arr = [1,2,3,4,6,99]
print(arr[-1])
# %%

q = [0] * 99
q

# %%
def minCostClimbingStairs(cost):
  dp = [0] * len(cost)
  dp[0] = cost[0]
  dp[1] = cost[1]
  for i in range(2, len(cost)):
    dp[i] = cost[i] + min(dp[i-1], dp[i-2])
  return min(dp[-1], dp[-2])


# %%
for i in range(2, 10):
  print(i)
# %%
def tribonacci(n):
  dp = [0] * (n+1)
  dp[0] = 0
  dp[1] = 1
  dp[2] = 1
  for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  return dp[n]


def deleteAndEarn(self, nums):
    """
        :type nums: List[int]
        :rtype: int
        """
    if not nums:
        return 0
    max_num = max(nums)
    count = [0] * (max_num + 1)
    for num in nums:
        count[num] += num
    dp = [0] * (max_num + 1)
    dp[1] = count[1]
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + count[i])
    return dp[max_num]


# %%
li = [1,2,3,4,5]
max(li)
# %%
