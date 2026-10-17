class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start: int, curr_combo: list) -> None:
            res.append(curr_combo.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                curr_combo.append(nums[i])
                backtrack(i + 1, curr_combo)

                curr_combo.pop()

        backtrack(0, [])
        return res