class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        1->2->3->4->5  2,4
        1->4->3->2->5
        """
        res=ListNode(0)
        res.next=head
        point=res
        for __ in range(m-1):
            point=point.next
        pre=point.next
        curr=pre.next
        for __ in range(n-m):
            next=curr.next
            curr.next=pre
            pre=curr
            curr=next
        point.next.next=pre
        point.next=curr
