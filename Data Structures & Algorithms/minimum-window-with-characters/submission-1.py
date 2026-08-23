from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        missing = len(t)        # chars still owed, counting duplicates
        start, end = 0, 0       # best window as [start, end)
        l = 0

        for r, ch in enumerate(s):
            if need[ch] > 0:    # this char was actually needed
                missing -= 1
            need[ch] -= 1       # goes negative for surplus chars

            while missing == 0:             # valid window — now shrink it
                if end == 0 or r - l + 1 < end - start:
                    start, end = l, r + 1
                need[s[l]] += 1
                if need[s[l]] > 0:          # we just gave up a needed char
                    missing += 1
                l += 1

        return s[start:end]