class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i: int, curr_combo: list, curr_sum: int) -> None:
            if curr_sum == target:
                res.append(curr_combo.copy())
                return

            if i >= len(nums) or curr_sum > target:
                return
            
            curr_combo.append(nums[i])
            backtrack(i, curr_combo, curr_sum + nums[i])

            curr_combo.pop()
            backtrack(i + 1, curr_combo, curr_sum)
        
        backtrack(0, [], 0)
        return res