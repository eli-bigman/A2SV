# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = head
        even  = odd.next
        even_head = head.next

        while even and even.next:
            #build even list
            odd.next = even.next
            odd = odd.next

            #build odd list
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head
