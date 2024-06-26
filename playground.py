

'''
prepared
'''

# %%
# # 1. Two Sum


import helper
# %%


def twoSum(nums, target):
  ans = []
  for i in range(len(nums)):
      for j in (range(i+1, len(nums))):
          if nums[i] + nums[j] == target:
              return [i, j]


# U usage of twoSum
nums = [2, 7, 11, 15]
target = 9
twoSum(nums, target)

# %%
# 2. Add Two Numbers
# helper.py defined a ListNode(object), feel free to use .


def addTwoNumbers(l1, l2):

  '''
  l1: ListNode
  l2: ListNode
  '''
  # create a new ListNode
  dummy = helper.ListNode(0)
  curr = dummy
  carry = 0
  while l1 or l2 or carry:
    if l1:
        carry += l1.val
        l1 = l1.next
    if l2:
        carry += l2.val
        l2 = l2.next
    curr.next = helper.ListNode(carry % 10)
    curr = curr.next
    carry = carry // 10


l1 = helper.ListNode(2)
l1.next = helper.ListNode(4)
l1.next.next = helper.ListNode(3)
l2 = helper.ListNode(5)
l2.next = helper.ListNode(6)
l2.next.next = helper.ListNode(4)

ans = addTwoNumbers(l1, l2)
ans.val
# %%

280 // 10
# %%
10 % 9
# %%

7 % 10
# %%

7 % 10

# %%

# %%
s = "[](){}"
s[0]

# %%


def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    print(stack)
    return not stack


s = '[]{()'
isValid(s)
# %%


def check_validity(s):
  split = list(s)
  lookup = {')': '(', ']': '[', '}': '{'}
  ans = False
  for idx, c in enumerate(split):
    if c in lookup and lookup[c] == split[idx-1]:
        ans = True
    else:
        ans = False
  return ans


check_validity('[]{}()')


# %%
# reserve an string
def reverse(s):
  words = [word for word in s.split(' ') if word]
  return ' '.join(words[::-1])


# %%
s = list('Hello World ! 123')
a = ''.join(word for word in s if word.isalnum())
a == a[::-1]
# O(n), O(n) which n is the length of s

# %%
s = '234 with word'
s.isalnum()

''.join(word)
# %%


def myAtoi(s):
  s = s.strip()
  if not s:
    return 0
  sign = -1 if s[0] == '-' else 1
  if s[0] in ['-', '+']:
    s = s[1:]
  res = 0
  for i in range(len(s)):
    if not s[i].isdigit():
        break
    res = res * 10 + int(s[i])
  return max(-2**31, min(sign * res, 2**31-1))


# %%
la = list('11223344abc')
list.insert(la, 0, 'mas')


# %%

nums = [1, 1, 0, 1, 1, 1, 0]


def countOne(nums):
  current_length = 0
  max_length = 0
  for i in range(len(nums)):
    if nums[i] == 1:
      current_length += 1
      max_length = max(max_length, current_length)
    else:
      current_length = 0

  return max_length


x = countOne(nums)
x
# %%
a = 0
print(a)
b = 1
print(b)
for i in range(20):
  # complete the code in this loop
  c = a + b
  a = b
  b = c
  print(c)

# %%
a = 0
b = 1
c = a + b

b = c
a = c

# %%
wallet = 8

for price in range(10):
  if wallet >= price:
    wallet = wallet - price
    print("I have", wallet, "left")
  else:
    print("I can't afford any more")
    break

# %%
wallet = 25
socks = 0

for price in range(10):
    if wallet >= price:
      wallet = wallet - price
      socks = socks + 1
    else:
      break

if (socks % 2 == 0):   # fill in this condition
  print("I can pair my socks")
else:
  print("I need one more...")

# %%


number = 3
steps = 0

for i in range(200):
    if number == 1:
      break
    # fill in the rest of this program
    elif number % 2 == 0:
      number = number / 2
      print(number)
      steps += 1
    elif number % 2 == 1:
      number *= 3
      number += 1
      print(number)
      steps += 1

if number == 1:
  print("It took", steps, "steps")
else:
  print("The number didn't reach 1 yet")

# %%
for i in range(0, 100, -5):
  print(i)

# %%
#  Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(s):
  if not s:
    return 0
  max_length = 0
  start = 0
  seen = set()
  for end in range(len(s)):
    while s[end] in seen:
      print('now in', s[end], ' going to remove', s[start], seen)
      seen.remove(s[start])
      print('removed', s[start], 'now seen = ', seen)
      start += 1
      print('new start',  start)
    print('going to add', s[end])
    seen.add(s[end])
    print('now seen = ', seen)
    print('max_length', max_length, 'end - start + 1', end - start + 1)
    max_length = max(max_length, end - start + 1)
  return max_length


lengthOfLongestSubstring('abcdfjabc')
# %%
s = "hello"
reversed = s[::-1]
s[1:3]

# %%
s = set()
s.add('a')
s.add('b')
s.add('c')
print(s)
s.remove('c')
print(s)
# %%


def max_sub_array_of_size_k(k, nums):
  max_sum = float('-inf')
  window_sum = 0
  window_start = 0

  for window_end in range(len(nums)):
    window_sum += nums[window_end]  # Add the next element to the window

    # Slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if window_end >= k - 1:
      # Update the maximum sum if necessary
      max_sum = max(max_sum, window_sum)
      # Subtract the element going out of the window
      window_sum -= nums[window_start]
      window_start += 1  # Slide the window ahead

  return max_sum


# Example usage
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 5
print(max_sub_array_of_size_k(k, nums))  # Output: 39

# %%
arr = list(range(10))
q = len(arr)
arr

# %%
def missingNumber(nums):
  n = len(nums)
  total_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  return total_sum - actual_sum

nums = [3, 0, 1]
missing_number = missingNumber(nums)
print(missing_number)
# %%
arr = [1,4,0]
len(arr)
# %%
a = [1,2,3,4,5,6]
sum(a)
# %%
s = "Hello, World!"

list(s)
# %%

a = [1,2,3]
sum_result = sum(a)
print(sum_result)
# %%
def fairCandySwap(A, B):
  sum_A, sum_B = sum(A), sum(B)
  set_B = set(B)
  for x in A:
    if x + (sum_B - sum_A) // 2 in set_B:
      return [x, x + (sum_B - sum_A) // 2]
        
# %%

set_B = set([1,2,3,4,5])
set_B
# %%

names = ["Mary", "John", "Emma"]
heights = [421, 165, 170]

# Zip names and heights together and sort by height
paired = zip(names, heights)
a = list(paired)
# sorted_pairs = sorted(paired, key=lambda x: x[1], reverse=True)

print(a)

# %%
sen = 'I fuck you mother last night, and she eat all my cum, lun dui Choi Yuk Kei you are pokGuyHamKaChan!!!!'

sen = ''.join(char for char in sen if char.isalnum() or char.isspace() )
print(sen) 

words = sen.split()

ans =  max(words, key = len)

ans

# %%


# %%
import random
arr = [random.randint(0, 100) for _ in range(10)] 
mid = len(arr) // 2 
L = arr[::mid] 
R = arr[mid:] 

i = j = k = 0

while i < len(L) and j < len(R):
  if L[i] < R[j]:
    arr[k] = L[i]
    i += 1
  else:
    arr[k] = R[j]
    j += 1
  k += 1
while i < len(L):
  arr[k] = L[i]
  i += 1
  j += 1
while j < len(R):
  arr[k] = R[r]
  i += 1
  j += 1





# %%


def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()

# %%
for u in range(9):
  print(u)
# %%
from functools import reduce
# Sum all numbers in a list
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)


# %%
def generate(numRows):
  ans =  []
  for i in range(numRows):
    print('i', i)
    ans.append([1] * (i + 1))
    for j in range(1, i):
      print('j', i)
      ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
  return ans
    

generate(5)
# %%
def t():
  for i in range(1, 2):
    print(i)
t()
# %%
strs = '美國聯合航空再有波音客機飛行期間發生事故，外部面板飛脫，已安全緊急降落'
print(''.join(char for char in strs if char.isalnum()))

# %%
s = 'abcdefghijklmnopqrstuvwxyz'
def find_duplicate(s):
  duplicate_chars = []
  for i in range(len(s)):
    if s[i] in s[i+1:] and s[i] not in duplicate_chars:
      duplicate_chars.append(s[i])
  return duplicate_chars

duplicate_chars = find_duplicate(s)
print(duplicate_chars)
# %%
def is_permutation(str1, str2):
  return sorted(str1) == sorted(str2)

str1 = "abc"
str2 = "bca"
if is_permutation(str1, str2):
  print("One string is a permutation of the other")
else:
  print("One string is not a permutation of the other")