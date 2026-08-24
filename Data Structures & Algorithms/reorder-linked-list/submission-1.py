# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current=head
        count=0
        prev=None

        huzz=ListNode()
        
        while current  :
            count+=1
            current=current.next
        slow=fast=head
        # i have to find the mid of the list
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        if count%2==0:
            slow=slow.next    

        new=slow
        new=new.next
        slow.next=None
        #now reverse the 2nd linked list
        while new is not None:
            nxt=new.next
            new.next=prev
            prev=new
            new=nxt
        #prev is the head of the new list , now add in first list
        cut=head
        huzz=prev
        while prev is not None:
                
                huzz=huzz.next
                prev.next=cut.next
                cut.next=prev
                cut=prev.next
                prev=huzz
                




        
       

                
            

            

            

