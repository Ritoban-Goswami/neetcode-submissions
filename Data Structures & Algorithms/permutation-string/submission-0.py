class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = [0] * 26
        countS2 = [0] * 26

        for c in s1:
            countS1[ord(c) - ord('a')] += 1

        l=0
        for r in range(len(s2)):
            countS2[ord(s2[r]) - ord('a')] += 1

            if  r - l + 1 > len(s1):
                countS2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if countS1 == countS2:
                return True

        return False