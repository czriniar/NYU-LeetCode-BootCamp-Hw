# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
         # Helper function to reverse a sublist of the linked list
        def reverse_sublist(start, end):
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # Function to get the length of the linked list
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        # Get the length of the linked list
        length = get_length(head)

        # Dummy node to handle edge cases and simplify code
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        curr = head

        while length >= k:
            group_end = curr
            for _ in range(k - 1):
                group_end = group_end.next

            nxt = group_end.next

            # Reverse the current group
            new_head = reverse_sublist(curr, nxt)

            # Connect the reversed group to the rest of the list
            prev_group_end.next = new_head
            curr.next = nxt

            # Move pointers for the next iteration
            prev_group_end = curr
            curr = nxt
            length -= k

        return dummy.next
