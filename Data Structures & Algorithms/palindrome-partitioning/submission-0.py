class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current_path = []

        def is_palindrome(left_idx: int, right_idx: int) -> bool:
            while left_idx < right_idx:
                if s[left_idx] != s[right_idx]:
                    return False
                left_idx += 1
                right_idx -= 1
            return True

        def backtrack(start_idx: int) -> None:
            if start_idx == len(s):
                result.append(current_path.copy())
                return
            
            for end_idx in range(start_idx, len(s)):
                if is_palindrome(start_idx, end_idx):
                    current_path.append(s[start_idx:end_idx + 1])
                    backtrack(end_idx + 1)
                    current_path.pop()

        backtrack(0)
        return result