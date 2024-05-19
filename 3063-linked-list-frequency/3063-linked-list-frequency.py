# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = {}
        ptr = head
        while ptr != None:
            if ptr.val not in freq:
                freq[ptr.val] = 1
            else:
                freq[ptr.val] += 1
            ptr = ptr.next
        
        res = ListNode(0)
        curr_ptr = res
        for val in freq.values():
            curr_ptr.next = ListNode(val)
            curr_ptr = curr_ptr.next
        
        return res.next
        