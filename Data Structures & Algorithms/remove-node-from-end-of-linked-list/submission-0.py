# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        new=head 
        if (count-n)==0:
            new=new.next
            return new
           


        for i in range(count-n-1)  :
            new=new.next
        if (count-n) ==count:
            return new   
        nxt=new.next
        new.next=nxt.next
        nxt=None
        return head
            





        