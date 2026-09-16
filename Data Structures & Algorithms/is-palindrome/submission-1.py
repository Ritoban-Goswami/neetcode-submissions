class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitizedStr = ""

        for c in s:
            if c.isalnum():
                sanitizedStr += c.lower()
        return sanitizedStr == sanitizedStr[::-1]