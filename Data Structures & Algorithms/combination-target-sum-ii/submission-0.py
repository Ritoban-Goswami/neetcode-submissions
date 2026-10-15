class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(start_idx: int, current_combo: list, remaining_sum: int) -> None:
            if remaining_sum == 0:
                res.append(current_combo.copy())
                return

            for i in range(start_idx, len(candidates)):
                if candidates[i] > remaining_sum:
                    break

                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue

                current_combo.append(candidates[i])
                backtrack(i + 1, current_combo, remaining_sum - candidates[i])
                current_combo.pop()

        backtrack(0, [], target)
        return res