def isPalindrome(self, head):
  """
  :type head: ListNode
  :rtype: bool
  """ 

  if head is None:
    return True

  slow = fast = head = head
  # find the middle of the list, reverse the second half  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  # reverse the second half
  prev = None
  while slow:
    temp = slow.next
    slow.next = prev
    prev = slow
    slow = temp

  # compare the first and second half
  left, right = head, prev
  while right:
    if left.val != right.val:
      return False
    left = left.next
    right = right.next
  return True

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), no extra space is used.
