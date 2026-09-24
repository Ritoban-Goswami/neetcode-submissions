class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            midRow = (top + bottom) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bottom = midRow - 1
            else:
                break
        
        if not top <= bottom:
            return False
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[midRow][m]:
                l = m + 1
            elif target < matrix[midRow][m]:
                r = m - 1
            else:
                return True
        return False