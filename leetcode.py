

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
