class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for l in matrix:
            if l[-1] < target:
                continue 
            elif l[-1] == target:
                return True
            else: #search this one
                for n in l:
                    if n == target:
                        return True
                return False
        return False