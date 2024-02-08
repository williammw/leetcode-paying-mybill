

'''
record of my leetcode practice

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
        print(seen)
        while s[end] in seen:
            # print(seen)
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        max_length = max(max_length, end - start + 1)
    return max_length


lengthOfLongestSubstring('abcabcbb')
# %%
