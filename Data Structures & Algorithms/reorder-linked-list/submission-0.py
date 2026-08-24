class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. length
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # 2. split — first half keeps the extra node when n is odd
        tail1 = head
        for _ in range((n + 1) // 2 - 1):
            tail1 = tail1.next
        second = tail1.next
        tail1.next = None

        # 3. reverse the second half
        prev = None
        while second:
            nxt = second.next      # save before overwriting
            second.next = prev
            prev = second
            second = nxt
        second = prev

        # 4. weave the two halves
        first = head
        while second:
            f_next = first.next    # save BOTH successors first
            s_next = second.next
            first.next = second
            second.next = f_next
            first = f_next
            second = s_next