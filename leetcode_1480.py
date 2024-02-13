def runningSum(self, nums):
  """
  :type nums: List[int]
  :rtype: List[int]
  """
  ans = []
  numsum = 0
  for i in range(len(nums)):

      if i == 0:
          ans.append(nums[i])
          numsum = nums[i]
          continue

      print(i)
      localsum = numsum + nums[i]
      # update numsum to localsum
      numsum = localsum
      ans.append(localsum)

  return ans
