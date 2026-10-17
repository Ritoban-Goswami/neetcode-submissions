class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(current_combo: list, used_nums: list) -> None:
            if len(current_combo) == len(nums):
                res.append(current_combo.copy())
                return

            for i in range(len(nums)):
                if used_nums[i]: continue
                
                current_combo.append(nums[i])
                used_nums[i] = True
                backtrack(current_combo, used_nums)

                current_combo.pop()
                used_nums[i] = False
        
        backtrack([], [False] * len(nums))
        return res