class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) ->bool:
        
        for n in matrix:
            for m in n:
                if m==target:
                    return True
        return False
        