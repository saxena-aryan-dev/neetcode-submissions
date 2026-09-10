class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        new = slow.next
        slow.next = None

        prev = None
        while new:
            nxt = new.next
            new.next = prev
            prev = new
            new = nxt

        cut = head
        while prev:
            huzz = prev.next
            prev.next = cut.next
            cut.next = prev
            cut = prev.next
            prev = huzz