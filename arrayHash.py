class Solution(object):
  def lengthOfLongestSubstring(self,s):
    """
    :type s: str
    :rtype: int
    """
    
    if not s:
      return 0
    
    max_length = 0
    start = 0
    seen = set()

    for end in range(len(s)):
      while s[end] in seen:
        seen.remove(s[start])
        start += 1
      seen.add(s[end])
      max_length = max(max_length, end - start + 1)
    return max_length
  



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

  def threeSum(self, nums):
    # Sort the array to make handling duplicates easier and for two-pointer approach.
    nums.sort()
    # Initialize an empty list to store the triplets that sum up to zero.
    result = []

    # Iterate through each number in the array to consider it as the first number of the triplet.
    for i in range(len(nums)):
        # If the current number is the same as the one before it, skip it to avoid duplicate triplets.
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Initialize two pointers, left and right, to find the other two numbers.
        left, right = i + 1, len(nums) - 1

        # While the left pointer is to the left of the right pointer.
        while left < right:
            # Calculate the sum of the numbers at the three pointers.
            total = nums[i] + nums[left] + nums[right]

            # If the sum is less than zero, move the left pointer to the right to increase the sum.
            if total < 0:
                left += 1
            # If the sum is greater than zero, move the right pointer to the left to decrease the sum.
            elif total > 0:
                right -= 1
            # If the sum is zero, we've found a valid triplet.
            else:
                # Add the triplet to the result list.
                result.append([nums[i], nums[left], nums[right]])

                # Skip over any duplicate numbers for the second number in the triplet.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip over any duplicate numbers for the third number in the triplet.
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers to look for new potential pairs after finding a valid triplet.
                left += 1
                right -= 1

    # Return the list of triplets that sum to zero.
    return result

  def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        start = None
        
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        if len(seen) == 0:
            return False
        
  def missingNumber(self, nums):
      """
        :type nums: List[int]
        :rtype: int
        """
      n = len(nums)
      total_sum = n * (n + 1) // 2
      actual_sum = sum(nums)
      return total_sum - actual_sum

  # 500. Keyboard Row
  def findWords(self, words):
      """
        :type words: List[str]
        :rtype: List[str]
        """
      first = 'qwertyuiop'
      second = 'asdfghjkl'
      third = 'zxcvbnm'

      ans = list()

      for word in words:
            a = 0
            b = 0
            c = 0
            for char in list(word.lower()):
                print(char)
                if char in first:
                    a += 1
                elif char in second:
                    b += 1
                elif char in third:
                    c += 1
            print(a, b, c)
            if a >= 1 and b == 0 and c == 0:
                ans.append(word)
            elif a == 0 and b >= 1 and c == 0:
                ans.append(word)
            elif a == 0 and b == 0 and c >= 1:
                ans.append(word)
      return ans
  
  def sortPeople(self, names, heights):
    """
    :type names: List[str]
    :type heights: List[int]
    :rtype: List[str]
    """

    paired = zip(names, heights)
    sorted_pairs = sorted(paired, key=lambda x: x[1], reverse=True)

    sorted_names, sorted_heights = zip(*sorted_pairs)

    sorted_names = list(sorted_names)
    return sorted_names

  def LongestWord(sen):
    # Removing punctuation from the input string
    sen = ''.join(char for char in sen if char.isalnum() or char.isspace())

    # Splitting the string into words
    words = sen.split()

    # Finding the longest word
    longest_word = max(words, key=len)

    return longest_word

