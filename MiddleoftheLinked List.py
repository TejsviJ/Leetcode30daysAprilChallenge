class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow=fast=head
        while fast and fast.next:
            print (fast,slow)
            fast=fast.next.next
            slow=slow.next
        return slow
