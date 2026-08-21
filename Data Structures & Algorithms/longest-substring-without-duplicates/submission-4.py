class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        maxi = 0
        for r, ch in enumerate(s):
            if ch in seen and seen[ch] >= l:
                l = seen[ch] + 1
            seen[ch] = r
            maxi = max(maxi, r - l + 1)
        return maxi