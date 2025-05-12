# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while True:

            stack  = []
            temp = curr

            for _ in range(k):
                if not temp:
                    return dummy.next
                stack.append(temp)
                temp = temp.next

            while stack:
                prev.next = stack.pop()
                prev = prev.next


            prev.next = temp

            curr = temp