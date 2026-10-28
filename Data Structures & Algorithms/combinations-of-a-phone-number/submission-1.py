class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        result = []
        current_combination = []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        def backtrack(idx: int) -> None:
            if idx == len(digits):
                result.append("".join(current_combination))
                return

            digit = digits[idx]
            letters = phone_map[digit]

            for letter in letters:
                current_combination.append(letter)
                backtrack(idx + 1)
                current_combination.pop()
            
        backtrack(0)
        return result