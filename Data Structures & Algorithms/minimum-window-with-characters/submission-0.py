class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        window = {}
        l = 0
        have = 0
        res = ""
        resL = float('inf')
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == len(countT):
                if resL > r - l + 1:
                    res = s[l:r+1]
                    resL = r - l + 1
                
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        return res