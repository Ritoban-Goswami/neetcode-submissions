class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx: int, current_subset: list) -> None:
            if idx > len(nums) - 1:
                res.append(current_subset.copy())
                return
            
            current_subset.append(nums[idx])
            backtrack(idx + 1, current_subset)

            current_subset.pop()
            backtrack(idx + 1, current_subset)

        backtrack(0, [])
        return res