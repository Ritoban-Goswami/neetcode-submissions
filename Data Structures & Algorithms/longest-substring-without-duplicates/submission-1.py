class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            seen = {}
            res, l = 0, 0
            for r, c in enumerate(s):
                if c in seen:
                    l = max(l, seen[c] + 1)

                seen[c] = r
                res = max(res, r - l + 1)
            return res