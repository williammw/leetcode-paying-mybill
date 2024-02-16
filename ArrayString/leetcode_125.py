
def isPalindrome(self, s):
  """
  :type s: str
  :rtype: bool
  """
  # extract alphanumeric characters and convert to lowercase
  ans = ''.join(char for char in s if char.isalnum()).lower()
  return ans == ans[::-1]
