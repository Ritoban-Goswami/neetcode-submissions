class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr_str: str, open_cnt: int, close_cnt: int) -> None:
            if len(curr_str) == n*2:    
                res.append(curr_str)
                return
            
            if open_cnt < n:
                backtrack(curr_str + "(", open_cnt + 1, close_cnt)
            if close_cnt < open_cnt:
                backtrack(curr_str + ")", open_cnt, close_cnt + 1)

        backtrack('', 0, 0)
        return res