# %% 
from meta import Solution

solution = Solution()
print(solution.lengthOfLongestSubstring('abc'))
''' 
The `lengthOfLongestSubstring` function has a time 
complexity of O(n) and a space complexity of O(min(n, m)) because set() . 
'''

# %%


arr = [1000,1,3,7,8,-99,1000]
for i in range(len(arr)):
  if i > 0  and arr[i] == arr[i-1]:
    continue
# %%
